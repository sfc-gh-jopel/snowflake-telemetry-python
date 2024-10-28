# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from collections import defaultdict
from typing import Sequence, List

from m3.snowflake.telemetry.opentelemetry.exporter.otlp.proto.common._internal import (
    _encode_instrumentation_scope,
    _encode_resource,
    _encode_span_id,
    _encode_trace_id,
    _encode_value,
    _encode_attributes,
)

from opentelemetry.sdk._logs import LogData

from m3.snowflake.telemetry.serialize import ProtoSerializer


def encode_logs(batch: Sequence[LogData]) -> None:
    proto_serializer = ProtoSerializer()

    resource_logs = _process_resource_logs(batch)
    for resource_log in resource_logs:
        _encode_resource_logs(b"\n", proto_serializer, resource_log)
        # proto_serializer.serialize_message(b"\n", _encode_resource_logs, resource_log)

    return bytes(proto_serializer)


def _encode_log(tag, proto_serializer: ProtoSerializer, log_data: LogData) -> None:
    before = len(proto_serializer.out) - proto_serializer.i
    span_id = (
        None
        if log_data.log_record.span_id == 0
        else _encode_span_id(log_data.log_record.span_id)
    )
    trace_id = (
        None
        if log_data.log_record.trace_id == 0
        else _encode_trace_id(log_data.log_record.trace_id)
    )
    time_unix_nano=log_data.log_record.timestamp
    observed_time_unix_nano=log_data.log_record.observed_timestamp
    span_id=span_id
    trace_id=trace_id
    flags=int(log_data.log_record.trace_flags)
    body=log_data.log_record.body
    severity_text=log_data.log_record.severity_text
    attributes=log_data.log_record.attributes
    dropped_attributes_count=log_data.log_record.dropped_attributes
    severity_number=log_data.log_record.severity_number.value

    if observed_time_unix_nano:
        proto_serializer.serialize_fixed64(b"Y", observed_time_unix_nano)
    if span_id:
        proto_serializer.serialize_bytes(b"R", span_id)
    if trace_id:
        proto_serializer.serialize_bytes(b"J", trace_id)
    if flags:
        proto_serializer.serialize_fixed32(b"E", flags)
    if dropped_attributes_count:
        proto_serializer.serialize_uint32(b"8", dropped_attributes_count)
    
    _encode_attributes(b"2", proto_serializer, attributes)

    if body:
        _encode_value(b"*", proto_serializer, body)
        # proto_serializer.serialize_message(b"*", _encode_value, body)

    if severity_text:
        proto_serializer.serialize_string(b"\x1a", severity_text)
    if severity_number:
        proto_serializer.serialize_enum(b"\x10", severity_number)
    if time_unix_nano:
        proto_serializer.serialize_fixed64(b"\t", time_unix_nano)
    
    after = len(proto_serializer.out) - proto_serializer.i
    proto_serializer.write_tag_size(tag, after - before)


def _process_resource_logs(batch: Sequence[LogData]) -> List[tuple]:
    sdk_resource_logs = defaultdict(lambda: defaultdict(list))

    for sdk_log in batch:
        sdk_resource = sdk_log.log_record.resource
        sdk_instrumentation = sdk_log.instrumentation_scope or None

        sdk_resource_logs[sdk_resource][sdk_instrumentation].append(sdk_log)

    pb2_resource_logs = []

    for sdk_resource, sdk_instrumentations in sdk_resource_logs.items():
        scope_logs = []
        for sdk_instrumentation, sdk_logs in sdk_instrumentations.items():
            scope_logs.append(
                (sdk_instrumentation, sdk_logs)
            )
        pb2_resource_logs.append(
            (sdk_resource, scope_logs)
        )
    return pb2_resource_logs

def _encode_resource_logs(tag, proto_serializer: ProtoSerializer,resource_log) -> None:
    resource, scope_logs = resource_log

    schema_url = resource.schema_url
    before = len(proto_serializer.out) - proto_serializer.i
    if resource:
        _encode_resource(b"\n", proto_serializer, resource)
        # proto_serializer.serialize_message(b"\n", _encode_resource, resource)
    if schema_url:
        proto_serializer.serialize_string(b"\x1a", schema_url)
    
    for scope_log in scope_logs:
        instrumentation, logs = scope_log
        if instrumentation:
            _encode_instrumentation_scope(b"\n", proto_serializer, instrumentation)
            # proto_serializer.serialize_message(b"\n", _encode_instrumentation_scope, instrumentation)
        for log in logs:
            _encode_log(b"\x12", proto_serializer, log)
            # proto_serializer.serialize_message(b"\x12", _encode_log, log)
    after = len(proto_serializer.out) - proto_serializer.i
    proto_serializer.write_tag_size(tag, after - before)
