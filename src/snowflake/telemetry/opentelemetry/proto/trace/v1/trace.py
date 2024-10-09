# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources:
# plugin: python-serialize

from typing import List

from snowflake.telemetry.serialize import (
    Enum,
    MessageMarshaler,
    ProtoSerializer,
    util,
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
        super().__init__(self.calculate_size())

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.resource_spans:
            proto_serializer.serialize_repeated_message(b"\n", self.resource_spans)

    def calculate_size(self) -> int:
        size = 0
        if self.resource_spans:
            size += util.size_repeated_message(b"\n", self.resource_spans)
        return size


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
        super().__init__(self.calculate_size())

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.resource:
            proto_serializer.serialize_message(b"\n", self.resource)
        if self.scope_spans:
            proto_serializer.serialize_repeated_message(b"\x12", self.scope_spans)
        if self.schema_url:
            proto_serializer.serialize_string(b"\x1a", self.schema_url)

    def calculate_size(self) -> int:
        size = 0
        if self.resource:
            size += util.size_message(b"\n", self.resource)
        if self.scope_spans:
            size += util.size_repeated_message(b"\x12", self.scope_spans)
        if self.schema_url:
            size += util.size_string(b"\x1a", self.schema_url)
        return size


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
        super().__init__(self.calculate_size())

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.scope:
            proto_serializer.serialize_message(b"\n", self.scope)
        if self.spans:
            proto_serializer.serialize_repeated_message(b"\x12", self.spans)
        if self.schema_url:
            proto_serializer.serialize_string(b"\x1a", self.schema_url)

    def calculate_size(self) -> int:
        size = 0
        if self.scope:
            size += util.size_message(b"\n", self.scope)
        if self.spans:
            size += util.size_repeated_message(b"\x12", self.spans)
        if self.schema_url:
            size += util.size_string(b"\x1a", self.schema_url)
        return size


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
        super().__init__(self.calculate_size())

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.trace_id:
            proto_serializer.serialize_bytes(b"\n", self.trace_id)
        if self.span_id:
            proto_serializer.serialize_bytes(b"\x12", self.span_id)
        if self.trace_state:
            proto_serializer.serialize_string(b"\x1a", self.trace_state)
        if self.parent_span_id:
            proto_serializer.serialize_bytes(b'"', self.parent_span_id)
        if self.name:
            proto_serializer.serialize_string(b"*", self.name)
        if self.kind:
            proto_serializer.serialize_enum(b"0", self.kind)
        if self.start_time_unix_nano:
            proto_serializer.serialize_fixed64(b"9", self.start_time_unix_nano)
        if self.end_time_unix_nano:
            proto_serializer.serialize_fixed64(b"A", self.end_time_unix_nano)
        if self.attributes:
            proto_serializer.serialize_repeated_message(b"J", self.attributes)
        if self.dropped_attributes_count:
            proto_serializer.serialize_uint32(b"P", self.dropped_attributes_count)
        if self.events:
            proto_serializer.serialize_repeated_message(b"Z", self.events)
        if self.dropped_events_count:
            proto_serializer.serialize_uint32(b"`", self.dropped_events_count)
        if self.links:
            proto_serializer.serialize_repeated_message(b"j", self.links)
        if self.dropped_links_count:
            proto_serializer.serialize_uint32(b"p", self.dropped_links_count)
        if self.status:
            proto_serializer.serialize_message(b"z", self.status)
        if self.flags:
            proto_serializer.serialize_fixed32(b"\x85\x01", self.flags)

    def calculate_size(self) -> int:
        size = 0
        if self.trace_id:
            size += util.size_bytes(b"\n", self.trace_id)
        if self.span_id:
            size += util.size_bytes(b"\x12", self.span_id)
        if self.trace_state:
            size += util.size_string(b"\x1a", self.trace_state)
        if self.parent_span_id:
            size += util.size_bytes(b'"', self.parent_span_id)
        if self.name:
            size += util.size_string(b"*", self.name)
        if self.kind:
            size += util.size_enum(b"0", self.kind)
        if self.start_time_unix_nano:
            size += util.size_fixed64(b"9", self.start_time_unix_nano)
        if self.end_time_unix_nano:
            size += util.size_fixed64(b"A", self.end_time_unix_nano)
        if self.attributes:
            size += util.size_repeated_message(b"J", self.attributes)
        if self.dropped_attributes_count:
            size += util.size_uint32(b"P", self.dropped_attributes_count)
        if self.events:
            size += util.size_repeated_message(b"Z", self.events)
        if self.dropped_events_count:
            size += util.size_uint32(b"`", self.dropped_events_count)
        if self.links:
            size += util.size_repeated_message(b"j", self.links)
        if self.dropped_links_count:
            size += util.size_uint32(b"p", self.dropped_links_count)
        if self.status:
            size += util.size_message(b"z", self.status)
        if self.flags:
            size += util.size_fixed32(b"\x85\x01", self.flags)
        return size

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
            super().__init__(self.calculate_size())

        def write_to(self, proto_serializer: ProtoSerializer) -> None:
            if self.time_unix_nano:
                proto_serializer.serialize_fixed64(b"\t", self.time_unix_nano)
            if self.name:
                proto_serializer.serialize_string(b"\x12", self.name)
            if self.attributes:
                proto_serializer.serialize_repeated_message(b"\x1a", self.attributes)
            if self.dropped_attributes_count:
                proto_serializer.serialize_uint32(b" ", self.dropped_attributes_count)

        def calculate_size(self) -> int:
            size = 0
            if self.time_unix_nano:
                size += util.size_fixed64(b"\t", self.time_unix_nano)
            if self.name:
                size += util.size_string(b"\x12", self.name)
            if self.attributes:
                size += util.size_repeated_message(b"\x1a", self.attributes)
            if self.dropped_attributes_count:
                size += util.size_uint32(b" ", self.dropped_attributes_count)
            return size

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
            super().__init__(self.calculate_size())

        def write_to(self, proto_serializer: ProtoSerializer) -> None:
            if self.trace_id:
                proto_serializer.serialize_bytes(b"\n", self.trace_id)
            if self.span_id:
                proto_serializer.serialize_bytes(b"\x12", self.span_id)
            if self.trace_state:
                proto_serializer.serialize_string(b"\x1a", self.trace_state)
            if self.attributes:
                proto_serializer.serialize_repeated_message(b'"', self.attributes)
            if self.dropped_attributes_count:
                proto_serializer.serialize_uint32(b"(", self.dropped_attributes_count)
            if self.flags:
                proto_serializer.serialize_fixed32(b"5", self.flags)

        def calculate_size(self) -> int:
            size = 0
            if self.trace_id:
                size += util.size_bytes(b"\n", self.trace_id)
            if self.span_id:
                size += util.size_bytes(b"\x12", self.span_id)
            if self.trace_state:
                size += util.size_string(b"\x1a", self.trace_state)
            if self.attributes:
                size += util.size_repeated_message(b'"', self.attributes)
            if self.dropped_attributes_count:
                size += util.size_uint32(b"(", self.dropped_attributes_count)
            if self.flags:
                size += util.size_fixed32(b"5", self.flags)
            return size


class Status(MessageMarshaler):
    def __init__(
        self,
        message: str = "",
        code: int = 0,
    ):
        self.message = message
        self.code = code
        super().__init__(self.calculate_size())

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.message:
            proto_serializer.serialize_string(b"\x12", self.message)
        if self.code:
            proto_serializer.serialize_enum(b"\x18", self.code)

    def calculate_size(self) -> int:
        size = 0
        if self.message:
            size += util.size_string(b"\x12", self.message)
        if self.code:
            size += util.size_enum(b"\x18", self.code)
        return size

    class StatusCode(Enum):
        STATUS_CODE_UNSET = 0
        STATUS_CODE_OK = 1
        STATUS_CODE_ERROR = 2
