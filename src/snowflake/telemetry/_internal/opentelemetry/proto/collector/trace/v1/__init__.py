# Generated by the protoc compiler with a custom plugin. DO NOT EDIT!
# sources: opentelemetry/proto/collector/trace/v1/trace_service.proto

from __future__ import annotations

from typing import (
    List,
    Optional,
)

from snowflake.telemetry._internal.opentelemetry.proto.trace.v1 import *
from snowflake.telemetry._internal.serialize import (
    Enum,
    MessageMarshaler,
    ProtoSerializer,
    util,
)


class ExportTraceServiceRequest(MessageMarshaler):
    def __init__(
        self,
        resource_spans: List[ResourceSpans] = None,
    ):
        self.resource_spans: List[ResourceSpans] = resource_spans
        super().__init__()

    def calculate_size(self) -> int:
        size = 0
        if self.resource_spans:
            size += util.size_repeated_message(b"\n", self.resource_spans)
        return size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.resource_spans:
            proto_serializer.serialize_repeated_message(b"\n", self.resource_spans)


class ExportTraceServiceResponse(MessageMarshaler):
    def __init__(
        self,
        partial_success: ExportTracePartialSuccess = None,
    ):
        self.partial_success: ExportTracePartialSuccess = partial_success
        super().__init__()

    def calculate_size(self) -> int:
        size = 0
        if self.partial_success is not None:
            size += util.size_message(b"\n", self.partial_success)
        return size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.partial_success is not None:
            proto_serializer.serialize_message(b"\n", self.partial_success)


class ExportTracePartialSuccess(MessageMarshaler):
    def __init__(
        self,
        rejected_spans: int = 0,
        error_message: str = "",
    ):
        self.rejected_spans: int = rejected_spans
        self.error_message: str = error_message
        super().__init__()

    def calculate_size(self) -> int:
        size = 0
        if self.rejected_spans:
            size += util.size_int64(b"\x08", self.rejected_spans)
        if self.error_message:
            size += util.size_string(b"\x12", self.error_message)
        return size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.rejected_spans:
            proto_serializer.serialize_int64(b"\x08", self.rejected_spans)
        if self.error_message:
            proto_serializer.serialize_string(b"\x12", self.error_message)