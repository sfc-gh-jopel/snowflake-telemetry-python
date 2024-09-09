from dataclasses import dataclass
from typing import List

import serialize

from snowflake.telemetry.proto.logs.v1 import logs_pb2


@dataclass
class ExportLogsServiceRequest(serialize.Message):
    resource_logs: List[logs_pb2.ResourceLogs] = serialize.message_field(1)


@dataclass
class ExportLogsServiceResponse(serialize.Message):
    partial_success: "ExportLogsPartialSuccess" = serialize.message_field(1)


@dataclass
class ExportLogsPartialSuccess(serialize.Message):
    rejected_log_records: int = serialize.int64_field(1)
    error_message: str = serialize.string_field(2)
