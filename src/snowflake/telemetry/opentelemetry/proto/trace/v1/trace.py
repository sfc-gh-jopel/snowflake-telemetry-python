# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources:
# plugin: python-serialize

from typing import List

from snowflake.telemetry.serialize import (
    Enum,
    MessageMarshaler,
    ProtoSerializer,
)


class SpanFlags(Enum):
    SPAN_FLAGS_DO_NOT_USE = 0
    SPAN_FLAGS_TRACE_FLAGS_MASK = 255
    SPAN_FLAGS_CONTEXT_HAS_IS_REMOTE_MASK = 256
    SPAN_FLAGS_CONTEXT_IS_REMOTE_MASK = 512


class TracesData(MessageMarshaler):
    def __init__(
        self,
        resource_spans: List[MessageMarshaler] = None,
    ):
        self.resource_spans = resource_spans

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.resource_spans:
            proto_serializer.serialize_repeated_message(b"\n", self.resource_spans)


class ResourceSpans(MessageMarshaler):
    def __init__(
        self,
        resource: MessageMarshaler = None,
        scope_spans: List[MessageMarshaler] = None,
        schema_url: str = "",
    ):
        self.resource = resource
        self.scope_spans = scope_spans
        self.schema_url = schema_url

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.schema_url:
            proto_serializer.serialize_string(b"\x1a", self.schema_url)
        if self.scope_spans:
            proto_serializer.serialize_repeated_message(b"\x12", self.scope_spans)
        if self.resource:
            proto_serializer.serialize_message(b"\n", self.resource)


class ScopeSpans(MessageMarshaler):
    def __init__(
        self,
        scope: MessageMarshaler = None,
        spans: List[MessageMarshaler] = None,
        schema_url: str = "",
    ):
        self.scope = scope
        self.spans = spans
        self.schema_url = schema_url

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.schema_url:
            proto_serializer.serialize_string(b"\x1a", self.schema_url)
        if self.spans:
            proto_serializer.serialize_repeated_message(b"\x12", self.spans)
        if self.scope:
            proto_serializer.serialize_message(b"\n", self.scope)


class Span(MessageMarshaler):
    def __init__(
        self,
        trace_id: bytes = b"",
        span_id: bytes = b"",
        trace_state: str = "",
        parent_span_id: bytes = b"",
        name: str = "",
        kind: int = 0,
        start_time_unix_nano: int = 0,
        end_time_unix_nano: int = 0,
        attributes: List[MessageMarshaler] = None,
        dropped_attributes_count: int = 0,
        events: List[MessageMarshaler] = None,
        dropped_events_count: int = 0,
        links: List[MessageMarshaler] = None,
        dropped_links_count: int = 0,
        status: MessageMarshaler = None,
        flags: int = 0,
    ):
        self.trace_id = trace_id
        self.span_id = span_id
        self.trace_state = trace_state
        self.parent_span_id = parent_span_id
        self.name = name
        self.kind = kind
        self.start_time_unix_nano = start_time_unix_nano
        self.end_time_unix_nano = end_time_unix_nano
        self.attributes = attributes
        self.dropped_attributes_count = dropped_attributes_count
        self.events = events
        self.dropped_events_count = dropped_events_count
        self.links = links
        self.dropped_links_count = dropped_links_count
        self.status = status
        self.flags = flags

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.flags:
            proto_serializer.serialize_fixed32(b"\x85\x01", self.flags)
        if self.status:
            proto_serializer.serialize_message(b"z", self.status)
        if self.dropped_links_count:
            proto_serializer.serialize_uint32(b"p", self.dropped_links_count)
        if self.links:
            proto_serializer.serialize_repeated_message(b"j", self.links)
        if self.dropped_events_count:
            proto_serializer.serialize_uint32(b"`", self.dropped_events_count)
        if self.events:
            proto_serializer.serialize_repeated_message(b"Z", self.events)
        if self.dropped_attributes_count:
            proto_serializer.serialize_uint32(b"P", self.dropped_attributes_count)
        if self.attributes:
            proto_serializer.serialize_repeated_message(b"J", self.attributes)
        if self.end_time_unix_nano:
            proto_serializer.serialize_fixed64(b"A", self.end_time_unix_nano)
        if self.start_time_unix_nano:
            proto_serializer.serialize_fixed64(b"9", self.start_time_unix_nano)
        if self.kind:
            proto_serializer.serialize_enum(b"0", self.kind)
        if self.name:
            proto_serializer.serialize_string(b"*", self.name)
        if self.parent_span_id:
            proto_serializer.serialize_bytes(b'"', self.parent_span_id)
        if self.trace_state:
            proto_serializer.serialize_string(b"\x1a", self.trace_state)
        if self.span_id:
            proto_serializer.serialize_bytes(b"\x12", self.span_id)
        if self.trace_id:
            proto_serializer.serialize_bytes(b"\n", self.trace_id)

    class SpanKind(Enum):
        SPAN_KIND_UNSPECIFIED = 0
        SPAN_KIND_INTERNAL = 1
        SPAN_KIND_SERVER = 2
        SPAN_KIND_CLIENT = 3
        SPAN_KIND_PRODUCER = 4
        SPAN_KIND_CONSUMER = 5

    class Event(MessageMarshaler):
        def __init__(
            self,
            time_unix_nano: int = 0,
            name: str = "",
            attributes: List[MessageMarshaler] = None,
            dropped_attributes_count: int = 0,
        ):
            self.time_unix_nano = time_unix_nano
            self.name = name
            self.attributes = attributes
            self.dropped_attributes_count = dropped_attributes_count

        def write_to(self, proto_serializer: ProtoSerializer) -> None:
            if self.dropped_attributes_count:
                proto_serializer.serialize_uint32(b" ", self.dropped_attributes_count)
            if self.attributes:
                proto_serializer.serialize_repeated_message(b"\x1a", self.attributes)
            if self.name:
                proto_serializer.serialize_string(b"\x12", self.name)
            if self.time_unix_nano:
                proto_serializer.serialize_fixed64(b"\t", self.time_unix_nano)

    class Link(MessageMarshaler):
        def __init__(
            self,
            trace_id: bytes = b"",
            span_id: bytes = b"",
            trace_state: str = "",
            attributes: List[MessageMarshaler] = None,
            dropped_attributes_count: int = 0,
            flags: int = 0,
        ):
            self.trace_id = trace_id
            self.span_id = span_id
            self.trace_state = trace_state
            self.attributes = attributes
            self.dropped_attributes_count = dropped_attributes_count
            self.flags = flags

        def write_to(self, proto_serializer: ProtoSerializer) -> None:
            if self.flags:
                proto_serializer.serialize_fixed32(b"5", self.flags)
            if self.dropped_attributes_count:
                proto_serializer.serialize_uint32(b"(", self.dropped_attributes_count)
            if self.attributes:
                proto_serializer.serialize_repeated_message(b'"', self.attributes)
            if self.trace_state:
                proto_serializer.serialize_string(b"\x1a", self.trace_state)
            if self.span_id:
                proto_serializer.serialize_bytes(b"\x12", self.span_id)
            if self.trace_id:
                proto_serializer.serialize_bytes(b"\n", self.trace_id)


class Status(MessageMarshaler):
    def __init__(
        self,
        message: str = "",
        code: int = 0,
    ):
        self.message = message
        self.code = code

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.code:
            proto_serializer.serialize_enum(b"\x18", self.code)
        if self.message:
            proto_serializer.serialize_string(b"\x12", self.message)

    class StatusCode(Enum):
        STATUS_CODE_UNSET = 0
        STATUS_CODE_OK = 1
        STATUS_CODE_ERROR = 2
