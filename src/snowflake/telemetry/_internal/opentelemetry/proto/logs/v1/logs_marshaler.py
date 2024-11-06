# Generated by the protoc compiler with a custom plugin. DO NOT EDIT!
# sources: opentelemetry/proto/logs/v1/logs.proto

from __future__ import annotations

import struct
from io import BytesIO
from typing import (
    List,
    Optional,
)

from snowflake.telemetry._internal.opentelemetry.proto.common.v1.common_marshaler import *
from snowflake.telemetry._internal.opentelemetry.proto.resource.v1.resource_marshaler import *
from snowflake.telemetry._internal.serialize import (
    Enum,
    MessageMarshaler,
    size_varint32,
    size_varint64,
    write_varint_unsigned,
)


class SeverityNumber(Enum):
    SEVERITY_NUMBER_UNSPECIFIED = 0
    SEVERITY_NUMBER_TRACE = 1
    SEVERITY_NUMBER_TRACE2 = 2
    SEVERITY_NUMBER_TRACE3 = 3
    SEVERITY_NUMBER_TRACE4 = 4
    SEVERITY_NUMBER_DEBUG = 5
    SEVERITY_NUMBER_DEBUG2 = 6
    SEVERITY_NUMBER_DEBUG3 = 7
    SEVERITY_NUMBER_DEBUG4 = 8
    SEVERITY_NUMBER_INFO = 9
    SEVERITY_NUMBER_INFO2 = 10
    SEVERITY_NUMBER_INFO3 = 11
    SEVERITY_NUMBER_INFO4 = 12
    SEVERITY_NUMBER_WARN = 13
    SEVERITY_NUMBER_WARN2 = 14
    SEVERITY_NUMBER_WARN3 = 15
    SEVERITY_NUMBER_WARN4 = 16
    SEVERITY_NUMBER_ERROR = 17
    SEVERITY_NUMBER_ERROR2 = 18
    SEVERITY_NUMBER_ERROR3 = 19
    SEVERITY_NUMBER_ERROR4 = 20
    SEVERITY_NUMBER_FATAL = 21
    SEVERITY_NUMBER_FATAL2 = 22
    SEVERITY_NUMBER_FATAL3 = 23
    SEVERITY_NUMBER_FATAL4 = 24


class LogRecordFlags(Enum):
    LOG_RECORD_FLAGS_DO_NOT_USE = 0
    LOG_RECORD_FLAGS_TRACE_FLAGS_MASK = 255


class LogsData(MessageMarshaler):
    @property
    def resource_logs(self) -> List[ResourceLogs]:
        if self._resource_logs is None:
            self._resource_logs = list()
        return self._resource_logs

    def __init__(
        self,
        resource_logs: List[ResourceLogs] = None,
    ):
        self._resource_logs: List[ResourceLogs] = resource_logs

    def calculate_size(self) -> int:
        size = 0
        if self._resource_logs:
            size += sum(
                message._get_size() + len(b"\n") + size_varint32(message._get_size())
                for message in self._resource_logs
            )
        return size

    def write_to(self, out: BytesIO) -> None:
        if self._resource_logs:
            for v in self._resource_logs:
                out += b"\n"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)


class ResourceLogs(MessageMarshaler):
    @property
    def resource(self) -> Resource:
        if self._resource is None:
            self._resource = Resource()
        return self._resource

    @property
    def scope_logs(self) -> List[ScopeLogs]:
        if self._scope_logs is None:
            self._scope_logs = list()
        return self._scope_logs

    schema_url: str

    def __init__(
        self,
        resource: Resource = None,
        scope_logs: List[ScopeLogs] = None,
        schema_url: str = "",
    ):
        self._resource: Resource = resource
        self._scope_logs: List[ScopeLogs] = scope_logs
        self.schema_url: str = schema_url

    def calculate_size(self) -> int:
        size = 0
        if self._resource is not None:
            size += (
                len(b"\n")
                + size_varint32(self._resource._get_size())
                + self._resource._get_size()
            )
        if self._scope_logs:
            size += sum(
                message._get_size() + len(b"\x12") + size_varint32(message._get_size())
                for message in self._scope_logs
            )
        if self.schema_url:
            v = self.schema_url.encode("utf-8")
            self._schema_url_encoded = v
            size += len(b"\x1a") + size_varint32(len(v)) + len(v)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self._resource is not None:
            out += b"\n"
            write_varint_unsigned(out, self._resource._get_size())
            self._resource.write_to(out)
        if self._scope_logs:
            for v in self._scope_logs:
                out += b"\x12"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.schema_url:
            v = self._schema_url_encoded
            out += b"\x1a"
            write_varint_unsigned(out, len(v))
            out += v


class ScopeLogs(MessageMarshaler):
    @property
    def scope(self) -> InstrumentationScope:
        if self._scope is None:
            self._scope = InstrumentationScope()
        return self._scope

    @property
    def log_records(self) -> List[LogRecord]:
        if self._log_records is None:
            self._log_records = list()
        return self._log_records

    schema_url: str

    def __init__(
        self,
        scope: InstrumentationScope = None,
        log_records: List[LogRecord] = None,
        schema_url: str = "",
    ):
        self._scope: InstrumentationScope = scope
        self._log_records: List[LogRecord] = log_records
        self.schema_url: str = schema_url

    def calculate_size(self) -> int:
        size = 0
        if self._scope is not None:
            size += (
                len(b"\n")
                + size_varint32(self._scope._get_size())
                + self._scope._get_size()
            )
        if self._log_records:
            size += sum(
                message._get_size() + len(b"\x12") + size_varint32(message._get_size())
                for message in self._log_records
            )
        if self.schema_url:
            v = self.schema_url.encode("utf-8")
            self._schema_url_encoded = v
            size += len(b"\x1a") + size_varint32(len(v)) + len(v)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self._scope is not None:
            out += b"\n"
            write_varint_unsigned(out, self._scope._get_size())
            self._scope.write_to(out)
        if self._log_records:
            for v in self._log_records:
                out += b"\x12"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.schema_url:
            v = self._schema_url_encoded
            out += b"\x1a"
            write_varint_unsigned(out, len(v))
            out += v


class LogRecord(MessageMarshaler):
    time_unix_nano: int
    severity_number: SeverityNumber
    severity_text: str

    @property
    def body(self) -> AnyValue:
        if self._body is None:
            self._body = AnyValue()
        return self._body

    @property
    def attributes(self) -> List[KeyValue]:
        if self._attributes is None:
            self._attributes = list()
        return self._attributes

    dropped_attributes_count: int
    flags: int
    trace_id: bytes
    span_id: bytes
    observed_time_unix_nano: int

    def __init__(
        self,
        time_unix_nano: int = 0,
        severity_number: SeverityNumber = 0,
        severity_text: str = "",
        body: AnyValue = None,
        attributes: List[KeyValue] = None,
        dropped_attributes_count: int = 0,
        flags: int = 0,
        trace_id: bytes = b"",
        span_id: bytes = b"",
        observed_time_unix_nano: int = 0,
    ):
        self.time_unix_nano: int = time_unix_nano
        self.severity_number: SeverityNumber = severity_number
        self.severity_text: str = severity_text
        self._body: AnyValue = body
        self._attributes: List[KeyValue] = attributes
        self.dropped_attributes_count: int = dropped_attributes_count
        self.flags: int = flags
        self.trace_id: bytes = trace_id
        self.span_id: bytes = span_id
        self.observed_time_unix_nano: int = observed_time_unix_nano

    def calculate_size(self) -> int:
        size = 0
        if self.time_unix_nano:
            size += len(b"\t") + 8
        if self.severity_number:
            v = self.severity_number
            if not isinstance(v, int):
                v = v.value
            size += len(b"\x10") + size_varint32(v)
        if self.severity_text:
            v = self.severity_text.encode("utf-8")
            self._severity_text_encoded = v
            size += len(b"\x1a") + size_varint32(len(v)) + len(v)
        if self._body is not None:
            size += (
                len(b"*")
                + size_varint32(self._body._get_size())
                + self._body._get_size()
            )
        if self._attributes:
            size += sum(
                message._get_size() + len(b"2") + size_varint32(message._get_size())
                for message in self._attributes
            )
        if self.dropped_attributes_count:
            size += len(b"8") + size_varint32(self.dropped_attributes_count)
        if self.flags:
            size += len(b"E") + 4
        if self.trace_id:
            size += len(b"J") + size_varint32(len(self.trace_id)) + len(self.trace_id)
        if self.span_id:
            size += len(b"R") + size_varint32(len(self.span_id)) + len(self.span_id)
        if self.observed_time_unix_nano:
            size += len(b"Y") + 8
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.time_unix_nano:
            out += b"\t"
            out += struct.pack("<Q", self.time_unix_nano)
        if self.severity_number:
            v = self.severity_number
            if not isinstance(v, int):
                v = v.value
            out += b"\x10"
            write_varint_unsigned(out, v)
        if self.severity_text:
            v = self._severity_text_encoded
            out += b"\x1a"
            write_varint_unsigned(out, len(v))
            out += v
        if self._body is not None:
            out += b"*"
            write_varint_unsigned(out, self._body._get_size())
            self._body.write_to(out)
        if self._attributes:
            for v in self._attributes:
                out += b"2"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.dropped_attributes_count:
            out += b"8"
            write_varint_unsigned(out, self.dropped_attributes_count)
        if self.flags:
            out += b"E"
            out += struct.pack("<I", self.flags)
        if self.trace_id:
            out += b"J"
            write_varint_unsigned(out, len(self.trace_id))
            out += self.trace_id
        if self.span_id:
            out += b"R"
            write_varint_unsigned(out, len(self.span_id))
            out += self.span_id
        if self.observed_time_unix_nano:
            out += b"Y"
            out += struct.pack("<Q", self.observed_time_unix_nano)
