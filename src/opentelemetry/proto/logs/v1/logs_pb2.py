from dataclasses import dataclass
from typing import List

import serialize

from opentelemetry.proto.common.v1 import common_pb2
from opentelemetry.proto.resource.v1 import resource_pb2


class SeverityNumber(serialize.Enum):
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


class LogRecordFlags(serialize.Enum):
    LOG_RECORD_FLAGS_DO_NOT_USE = 0
    LOG_RECORD_FLAGS_TRACE_FLAGS_MASK = 255


@dataclass
class LogsData(serialize.Message):
    resource_logs: List["ResourceLogs"] = serialize.message_field(1)


@dataclass
class ResourceLogs(serialize.Message):
    resource: resource_pb2.Resource = serialize.message_field(1)
    scope_logs: List["ScopeLogs"] = serialize.message_field(2)
    schema_url: str = serialize.string_field(3)


@dataclass
class ScopeLogs(serialize.Message):
    scope: common_pb2.InstrumentationScope = serialize.message_field(1)
    log_records: List["LogRecord"] = serialize.message_field(2)
    schema_url: str = serialize.string_field(3)


@dataclass
class LogRecord(serialize.Message):
    time_unix_nano: float = serialize.fixed64_field(1)
    observed_time_unix_nano: float = serialize.fixed64_field(11)
    severity_number: "SeverityNumber" = serialize.enum_field(2)
    severity_text: str = serialize.string_field(3)
    body: common_pb2.AnyValue = serialize.message_field(5)
    attributes: List[common_pb2.KeyValue] = serialize.message_field(6)
    dropped_attributes_count: int = serialize.uint32_field(7)
    flags: float = serialize.fixed32_field(8)
    trace_id: bytes = serialize.bytes_field(9)
    span_id: bytes = serialize.bytes_field(10)
