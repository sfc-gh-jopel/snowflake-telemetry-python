from dataclasses import dataclass
from typing import List

import serialize

from opentelemetry.proto.common.v1 import common_pb2 
from opentelemetry.proto.resource.v1 import resource_pb2


class SpanFlags(serialize.Enum):
    SPAN_FLAGS_DO_NOT_USE = 0
    SPAN_FLAGS_TRACE_FLAGS_MASK = 255
    SPAN_FLAGS_CONTEXT_HAS_IS_REMOTE_MASK = 256
    SPAN_FLAGS_CONTEXT_IS_REMOTE_MASK = 512


@dataclass
class TracesData(serialize.Message):
    resource_spans: List["ResourceSpans"] = serialize.message_field(1)


@dataclass
class ResourceSpans(serialize.Message):
    resource: resource_pb2.Resource = serialize.message_field(1)
    scope_spans: List["ScopeSpans"] = serialize.message_field(2)
    schema_url: str = serialize.string_field(3)


@dataclass
class ScopeSpans(serialize.Message):
    scope: common_pb2.InstrumentationScope = serialize.message_field(1)
    spans: List["Span"] = serialize.message_field(2)
    schema_url: str = serialize.string_field(3)


@dataclass
class Span(serialize.Message):
    trace_id: bytes = serialize.bytes_field(1)
    span_id: bytes = serialize.bytes_field(2)
    trace_state: str = serialize.string_field(3)
    parent_span_id: bytes = serialize.bytes_field(4)
    flags: float = serialize.fixed32_field(16)
    name: str = serialize.string_field(5)
    class SpanKind(serialize.Enum):
        SPAN_KIND_UNSPECIFIED = 0
        SPAN_KIND_INTERNAL = 1
        SPAN_KIND_SERVER = 2
        SPAN_KIND_CLIENT = 3
        SPAN_KIND_PRODUCER = 4
        SPAN_KIND_CONSUMER = 5
    kind: "SpanKind" = serialize.enum_field(6)
    start_time_unix_nano: float = serialize.fixed64_field(7)
    end_time_unix_nano: float = serialize.fixed64_field(8)
    attributes: List[common_pb2.KeyValue] = serialize.message_field(9)
    dropped_attributes_count: int = serialize.uint32_field(10)
    @dataclass
    class Event(serialize.Message):
        time_unix_nano: float = serialize.fixed64_field(1)
        name: str = serialize.string_field(2)
        attributes: List[common_pb2.KeyValue] = serialize.message_field(3)
        dropped_attributes_count: int = serialize.uint32_field(4)
    events: List["Event"] = serialize.message_field(11)
    dropped_events_count: int = serialize.uint32_field(12)
    @dataclass
    class Link(serialize.Message):
        trace_id: bytes = serialize.bytes_field(1)
        span_id: bytes = serialize.bytes_field(2)
        trace_state: str = serialize.string_field(3)
        attributes: List[common_pb2.KeyValue] = serialize.message_field(4)
        dropped_attributes_count: int = serialize.uint32_field(5)
        flags: float = serialize.fixed32_field(6)
    links: List["Link"] = serialize.message_field(13)
    dropped_links_count: int = serialize.uint32_field(14)
    status: "Status" = serialize.message_field(15)


@dataclass
class Status(serialize.Message):
    message: str = serialize.string_field(2)
    class StatusCode(serialize.Enum):
        STATUS_CODE_UNSET = 0
        STATUS_CODE_OK = 1
        STATUS_CODE_ERROR = 2
    code: "StatusCode" = serialize.enum_field(3)
