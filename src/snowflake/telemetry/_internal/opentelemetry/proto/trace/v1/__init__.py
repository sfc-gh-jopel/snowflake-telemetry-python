# Generated by the protoc compiler with a custom plugin. DO NOT EDIT!
# sources: opentelemetry/proto/trace/v1/trace.proto

from __future__ import annotations

import struct
from io import BytesIO
from typing import (
    List,
    Optional,
)

from snowflake.telemetry._internal.opentelemetry.proto.common.v1 import *
from snowflake.telemetry._internal.opentelemetry.proto.resource.v1 import *
from snowflake.telemetry._internal.serialize import (
    Enum,
    MessageMarshaler,
    size_varint32,
    size_varint64,
    write_varint_unsigned,
)


class SpanFlags(Enum):
    SPAN_FLAGS_DO_NOT_USE = 0
    SPAN_FLAGS_TRACE_FLAGS_MASK = 255
    SPAN_FLAGS_CONTEXT_HAS_IS_REMOTE_MASK = 256
    SPAN_FLAGS_CONTEXT_IS_REMOTE_MASK = 512


class TracesData(MessageMarshaler):
    def __init__(
        self,
        resource_spans: List[ResourceSpans] = None,
    ):
        self.resource_spans: List[ResourceSpans] = resource_spans

    def calculate_size(self) -> int:
        size = 0
        if self.resource_spans:
            size += sum(
                message._get_size() + len(b"\n") + size_varint32(message._get_size())
                for message in self.resource_spans
            )
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.resource_spans:
            for v in self.resource_spans:
                out.write(b"\n")
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)


class ResourceSpans(MessageMarshaler):
    def __init__(
        self,
        resource: Resource = None,
        scope_spans: List[ScopeSpans] = None,
        schema_url: str = "",
    ):
        self.resource: Resource = resource
        self.scope_spans: List[ScopeSpans] = scope_spans
        self.schema_url: str = schema_url

    def calculate_size(self) -> int:
        size = 0
        if self.resource is not None:
            size += (
                len(b"\n")
                + size_varint32(self.resource._get_size())
                + self.resource._get_size()
            )
        if self.scope_spans:
            size += sum(
                message._get_size() + len(b"\x12") + size_varint32(message._get_size())
                for message in self.scope_spans
            )
        if self.schema_url:
            v = self.schema_url.encode("utf-8")
            self._schema_url_encoded = v
            size += len(b"\x1a") + size_varint32(len(v)) + len(v)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.resource is not None:
            out.write(b"\n")
            write_varint_unsigned(out, self.resource._get_size())
            self.resource.write_to(out)
        if self.scope_spans:
            for v in self.scope_spans:
                out.write(b"\x12")
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.schema_url:
            v = self._schema_url_encoded
            out.write(b"\x1a")
            write_varint_unsigned(out, len(v))
            out.write(v)


class ScopeSpans(MessageMarshaler):
    def __init__(
        self,
        scope: InstrumentationScope = None,
        spans: List[Span] = None,
        schema_url: str = "",
    ):
        self.scope: InstrumentationScope = scope
        self.spans: List[Span] = spans
        self.schema_url: str = schema_url

    def calculate_size(self) -> int:
        size = 0
        if self.scope is not None:
            size += (
                len(b"\n")
                + size_varint32(self.scope._get_size())
                + self.scope._get_size()
            )
        if self.spans:
            size += sum(
                message._get_size() + len(b"\x12") + size_varint32(message._get_size())
                for message in self.spans
            )
        if self.schema_url:
            v = self.schema_url.encode("utf-8")
            self._schema_url_encoded = v
            size += len(b"\x1a") + size_varint32(len(v)) + len(v)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.scope is not None:
            out.write(b"\n")
            write_varint_unsigned(out, self.scope._get_size())
            self.scope.write_to(out)
        if self.spans:
            for v in self.spans:
                out.write(b"\x12")
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.schema_url:
            v = self._schema_url_encoded
            out.write(b"\x1a")
            write_varint_unsigned(out, len(v))
            out.write(v)


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
        attributes: List[KeyValue] = None,
        dropped_attributes_count: int = 0,
        events: List[Span.Event] = None,
        dropped_events_count: int = 0,
        links: List[Span.Link] = None,
        dropped_links_count: int = 0,
        status: Status = None,
        flags: int = 0,
    ):
        self.trace_id: bytes = trace_id
        self.span_id: bytes = span_id
        self.trace_state: str = trace_state
        self.parent_span_id: bytes = parent_span_id
        self.name: str = name
        self.kind: int = kind
        self.start_time_unix_nano: int = start_time_unix_nano
        self.end_time_unix_nano: int = end_time_unix_nano
        self.attributes: List[KeyValue] = attributes
        self.dropped_attributes_count: int = dropped_attributes_count
        self.events: List[Span.Event] = events
        self.dropped_events_count: int = dropped_events_count
        self.links: List[Span.Link] = links
        self.dropped_links_count: int = dropped_links_count
        self.status: Status = status
        self.flags: int = flags

    def calculate_size(self) -> int:
        size = 0
        if self.trace_id:
            size += len(b"\n") + size_varint32(len(self.trace_id)) + len(self.trace_id)
        if self.span_id:
            size += len(b"\x12") + size_varint32(len(self.span_id)) + len(self.span_id)
        if self.trace_state:
            v = self.trace_state.encode("utf-8")
            self._trace_state_encoded = v
            size += len(b"\x1a") + size_varint32(len(v)) + len(v)
        if self.parent_span_id:
            size += (
                len(b'"')
                + size_varint32(len(self.parent_span_id))
                + len(self.parent_span_id)
            )
        if self.name:
            v = self.name.encode("utf-8")
            self._name_encoded = v
            size += len(b"*") + size_varint32(len(v)) + len(v)
        if self.kind:
            v = self.kind
            if not isinstance(v, int):
                v = v.self.kind
            size += len(b"0") + size_varint32(v)
        if self.start_time_unix_nano:
            size += len(b"9") + 8
        if self.end_time_unix_nano:
            size += len(b"A") + 8
        if self.attributes:
            size += sum(
                message._get_size() + len(b"J") + size_varint32(message._get_size())
                for message in self.attributes
            )
        if self.dropped_attributes_count:
            size += len(b"P") + size_varint32(self.dropped_attributes_count)
        if self.events:
            size += sum(
                message._get_size() + len(b"Z") + size_varint32(message._get_size())
                for message in self.events
            )
        if self.dropped_events_count:
            size += len(b"`") + size_varint32(self.dropped_events_count)
        if self.links:
            size += sum(
                message._get_size() + len(b"j") + size_varint32(message._get_size())
                for message in self.links
            )
        if self.dropped_links_count:
            size += len(b"p") + size_varint32(self.dropped_links_count)
        if self.status is not None:
            size += (
                len(b"z")
                + size_varint32(self.status._get_size())
                + self.status._get_size()
            )
        if self.flags:
            size += len(b"\x85\x01") + 4
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.trace_id:
            out.write(b"\n")
            write_varint_unsigned(out, len(self.trace_id))
            out.write(self.trace_id)
        if self.span_id:
            out.write(b"\x12")
            write_varint_unsigned(out, len(self.span_id))
            out.write(self.span_id)
        if self.trace_state:
            v = self._trace_state_encoded
            out.write(b"\x1a")
            write_varint_unsigned(out, len(v))
            out.write(v)
        if self.parent_span_id:
            out.write(b'"')
            write_varint_unsigned(out, len(self.parent_span_id))
            out.write(self.parent_span_id)
        if self.name:
            v = self._name_encoded
            out.write(b"*")
            write_varint_unsigned(out, len(v))
            out.write(v)
        if self.kind:
            v = self.kind
            if not isinstance(v, int):
                v = v.self.kind
            out.write(b"0")
            write_varint_unsigned(out, v)
        if self.start_time_unix_nano:
            out.write(b"9")
            out.write(struct.pack("<Q", self.start_time_unix_nano))
        if self.end_time_unix_nano:
            out.write(b"A")
            out.write(struct.pack("<Q", self.end_time_unix_nano))
        if self.attributes:
            for v in self.attributes:
                out.write(b"J")
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.dropped_attributes_count:
            out.write(b"P")
            write_varint_unsigned(out, self.dropped_attributes_count)
        if self.events:
            for v in self.events:
                out.write(b"Z")
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.dropped_events_count:
            out.write(b"`")
            write_varint_unsigned(out, self.dropped_events_count)
        if self.links:
            for v in self.links:
                out.write(b"j")
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.dropped_links_count:
            out.write(b"p")
            write_varint_unsigned(out, self.dropped_links_count)
        if self.status is not None:
            out.write(b"z")
            write_varint_unsigned(out, self.status._get_size())
            self.status.write_to(out)
        if self.flags:
            out.write(b"\x85\x01")
            out.write(struct.pack("<I", self.flags))

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
            attributes: List[KeyValue] = None,
            dropped_attributes_count: int = 0,
        ):
            self.time_unix_nano: int = time_unix_nano
            self.name: str = name
            self.attributes: List[KeyValue] = attributes
            self.dropped_attributes_count: int = dropped_attributes_count

        def calculate_size(self) -> int:
            size = 0
            if self.time_unix_nano:
                size += len(b"\t") + 8
            if self.name:
                v = self.name.encode("utf-8")
                self._name_encoded = v
                size += len(b"\x12") + size_varint32(len(v)) + len(v)
            if self.attributes:
                size += sum(
                    message._get_size()
                    + len(b"\x1a")
                    + size_varint32(message._get_size())
                    for message in self.attributes
                )
            if self.dropped_attributes_count:
                size += len(b" ") + size_varint32(self.dropped_attributes_count)
            return size

        def write_to(self, out: BytesIO) -> None:
            if self.time_unix_nano:
                out.write(b"\t")
                out.write(struct.pack("<Q", self.time_unix_nano))
            if self.name:
                v = self._name_encoded
                out.write(b"\x12")
                write_varint_unsigned(out, len(v))
                out.write(v)
            if self.attributes:
                for v in self.attributes:
                    out.write(b"\x1a")
                    write_varint_unsigned(out, v._get_size())
                    v.write_to(out)
            if self.dropped_attributes_count:
                out.write(b" ")
                write_varint_unsigned(out, self.dropped_attributes_count)

    class Link(MessageMarshaler):
        def __init__(
            self,
            trace_id: bytes = b"",
            span_id: bytes = b"",
            trace_state: str = "",
            attributes: List[KeyValue] = None,
            dropped_attributes_count: int = 0,
            flags: int = 0,
        ):
            self.trace_id: bytes = trace_id
            self.span_id: bytes = span_id
            self.trace_state: str = trace_state
            self.attributes: List[KeyValue] = attributes
            self.dropped_attributes_count: int = dropped_attributes_count
            self.flags: int = flags

        def calculate_size(self) -> int:
            size = 0
            if self.trace_id:
                size += (
                    len(b"\n") + size_varint32(len(self.trace_id)) + len(self.trace_id)
                )
            if self.span_id:
                size += (
                    len(b"\x12") + size_varint32(len(self.span_id)) + len(self.span_id)
                )
            if self.trace_state:
                v = self.trace_state.encode("utf-8")
                self._trace_state_encoded = v
                size += len(b"\x1a") + size_varint32(len(v)) + len(v)
            if self.attributes:
                size += sum(
                    message._get_size() + len(b'"') + size_varint32(message._get_size())
                    for message in self.attributes
                )
            if self.dropped_attributes_count:
                size += len(b"(") + size_varint32(self.dropped_attributes_count)
            if self.flags:
                size += len(b"5") + 4
            return size

        def write_to(self, out: BytesIO) -> None:
            if self.trace_id:
                out.write(b"\n")
                write_varint_unsigned(out, len(self.trace_id))
                out.write(self.trace_id)
            if self.span_id:
                out.write(b"\x12")
                write_varint_unsigned(out, len(self.span_id))
                out.write(self.span_id)
            if self.trace_state:
                v = self._trace_state_encoded
                out.write(b"\x1a")
                write_varint_unsigned(out, len(v))
                out.write(v)
            if self.attributes:
                for v in self.attributes:
                    out.write(b'"')
                    write_varint_unsigned(out, v._get_size())
                    v.write_to(out)
            if self.dropped_attributes_count:
                out.write(b"(")
                write_varint_unsigned(out, self.dropped_attributes_count)
            if self.flags:
                out.write(b"5")
                out.write(struct.pack("<I", self.flags))


class Status(MessageMarshaler):
    def __init__(
        self,
        message: str = "",
        code: int = 0,
    ):
        self.message: str = message
        self.code: int = code

    def calculate_size(self) -> int:
        size = 0
        if self.message:
            v = self.message.encode("utf-8")
            self._message_encoded = v
            size += len(b"\x12") + size_varint32(len(v)) + len(v)
        if self.code:
            v = self.code
            if not isinstance(v, int):
                v = v.self.code
            size += len(b"\x18") + size_varint32(v)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.message:
            v = self._message_encoded
            out.write(b"\x12")
            write_varint_unsigned(out, len(v))
            out.write(v)
        if self.code:
            v = self.code
            if not isinstance(v, int):
                v = v.self.code
            out.write(b"\x18")
            write_varint_unsigned(out, v)

    class StatusCode(Enum):
        STATUS_CODE_UNSET = 0
        STATUS_CODE_OK = 1
        STATUS_CODE_ERROR = 2
