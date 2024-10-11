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


import logging
from collections.abc import Sequence
from itertools import count
from typing import (
    Any,
    Mapping,
    Optional,
    List,
    Callable,
    TypeVar,
    Dict,
    Iterator,
)

from opentelemetry.sdk.util.instrumentation import InstrumentationScope
from opentelemetry.sdk.trace import Resource
from opentelemetry.util.types import Attributes
from snowflake.telemetry.serialize import ProtoSerializer

_logger = logging.getLogger(__name__)

_TypingResourceT = TypeVar("_TypingResourceT")
_ResourceDataT = TypeVar("_ResourceDataT")


def _encode_instrumentation_scope(
    proto_serializer: ProtoSerializer,
    instrumentation_scope: InstrumentationScope,
) -> None:
    if instrumentation_scope is None:
        return
    if instrumentation_scope.name:
        proto_serializer.serialize_string(b"\n", instrumentation_scope.name)
    if instrumentation_scope.version:
        proto_serializer.serialize_string(b"\x12", instrumentation_scope.version)


def _encode_resource(proto_serializer, resource: Resource) -> None:
    _encode_attributes(b"\n", proto_serializer, resource.attributes)


def _encode_value(proto_serializer: ProtoSerializer, value: Any) -> None:
    if isinstance(value, bool):
        proto_serializer.serialize_bool(b"\x10", value)
    elif isinstance(value, str):
        proto_serializer.serialize_string(b"\n", value)
    elif isinstance(value, int):
        proto_serializer.serialize_int64(b"\x18", value)
    elif isinstance(value, float):
        proto_serializer.serialize_double(b"!", value)
    elif isinstance(value, Sequence):
        proto_serializer.serialize_message(b"*", _encode_array_value, value)
    elif isinstance(value, Mapping):
        proto_serializer.serialize_message(b"2", _encode_kvlist, value)
    else:
        raise Exception(f"Invalid type {type(value)} of value {value}")

def _encode_array_value(proto_serializer: ProtoSerializer, values: List[Any]) -> None:
    for value in values:
        proto_serializer.serialize_message(b"\n", _encode_value, value)
    
def _encode_kvlist(proto_serializer: ProtoSerializer, values: Mapping[str, Any]) -> None:
    for key, value in values.items():
        proto_serializer.serialize_message(b"\n", _encode_key_value, key, value)

def _encode_key_value(proto_serializer: ProtoSerializer, key: str, value: Any) -> None:
    if key:
        proto_serializer.serialize_string(b"\n", key)
    if value:
        proto_serializer.serialize_message(b"\x12", _encode_value, value)


def _encode_span_id(span_id: int) -> bytes:
    return span_id.to_bytes(length=8, byteorder="big", signed=False)


def _encode_trace_id(trace_id: int) -> bytes:
    return trace_id.to_bytes(length=16, byteorder="big", signed=False)


def _encode_attributes(
    tag: bytes,
    proto_serializer: ProtoSerializer,
    attributes: Attributes,
) -> None:
    if attributes:
        for key, value in attributes.items():
            # pylint: disable=broad-exception-caught
            try:
                proto_serializer.serialize_message(tag, _encode_key_value, key, value)
            except Exception as error:
                _logger.exception("Failed to encode key %s: %s", key, error)
