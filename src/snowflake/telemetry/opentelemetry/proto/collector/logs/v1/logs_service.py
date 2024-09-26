# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources:
# plugin: python-serialize

from typing import List

from snowflake.telemetry.serialize import (
    Enum,
    MessageMarshaler,
    ProtoSerializer,
)


class ExportLogsServiceRequest(MessageMarshaler):
    def __init__(
        self,
        resource_logs: List[MessageMarshaler] = None,
    ):
        self.resource_logs = resource_logs

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.resource_logs:
            proto_serializer.serialize_repeated_message(b"\n", self.resource_logs)


class ExportLogsServiceResponse(MessageMarshaler):
    def __init__(
        self,
        partial_success: MessageMarshaler = None,
    ):
        self.partial_success = partial_success

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.partial_success:
            proto_serializer.serialize_message(b"\n", self.partial_success)


class ExportLogsPartialSuccess(MessageMarshaler):
    def __init__(
        self,
        rejected_log_records: int = 0,
        error_message: str = "",
    ):
        self.rejected_log_records = rejected_log_records
        self.error_message = error_message

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.error_message:
            proto_serializer.serialize_string(b"\x12", self.error_message)
        if self.rejected_log_records:
            proto_serializer.serialize_int64(b"\x08", self.rejected_log_records)