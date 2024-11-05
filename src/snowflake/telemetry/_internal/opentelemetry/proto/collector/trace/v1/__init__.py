# Generated by the protoc compiler with a custom plugin. DO NOT EDIT!
# sources: opentelemetry/proto/collector/trace/v1/trace_service.proto

from __future__ import annotations

import struct
from io import BytesIO
from typing import (
    List,
    Optional,
)

from snowflake.telemetry._internal.opentelemetry.proto.trace.v1 import *
from snowflake.telemetry._internal.serialize import (
    Enum,
    MessageMarshaler,
    size_varint32,
    size_varint64,
    write_varint_unsigned,
)


class ExportTraceServiceRequest(MessageMarshaler):
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


class ExportTraceServiceResponse(MessageMarshaler):
    def __init__(
        self,
        partial_success: ExportTracePartialSuccess = None,
    ):
        self.partial_success: ExportTracePartialSuccess = partial_success

    def calculate_size(self) -> int:
        size = 0
        if self.partial_success is not None:
            size += (
                len(b"\n")
                + size_varint32(self.partial_success._get_size())
                + self.partial_success._get_size()
            )
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.partial_success is not None:
            out.write(b"\n")
            write_varint_unsigned(out, self.partial_success._get_size())
            self.partial_success.write_to(out)


class ExportTracePartialSuccess(MessageMarshaler):
    def __init__(
        self,
        rejected_spans: int = 0,
        error_message: str = "",
    ):
        self.rejected_spans: int = rejected_spans
        self.error_message: str = error_message

    def calculate_size(self) -> int:
        size = 0
        if self.rejected_spans:
            size += len(b"\x08") + size_varint64(
                self.rejected_spans + (1 << 64)
                if self.rejected_spans < 0
                else self.rejected_spans
            )
        if self.error_message:
            v = self.error_message.encode("utf-8")
            self._error_message_encoded = v
            size += len(b"\x12") + size_varint32(len(v)) + len(v)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.rejected_spans:
            out.write(b"\x08")
            write_varint_unsigned(
                out,
                (
                    self.rejected_spans + (1 << 64)
                    if self.rejected_spans < 0
                    else self.rejected_spans
                ),
            )
        if self.error_message:
            v = self._error_message_encoded
            out.write(b"\x12")
            write_varint_unsigned(out, len(v))
            out.write(v)
