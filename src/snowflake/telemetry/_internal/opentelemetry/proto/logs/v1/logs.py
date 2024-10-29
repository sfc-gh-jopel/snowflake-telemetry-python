# Generated by the protoc compiler with a custom plugin. DO NOT EDIT!
# sources: opentelemetry/proto/logs/v1/logs.proto

from typing import (
    List,
    Optional,
)

from snowflake.telemetry._internal.serialize import (
    Enum,
    ProtoSerializer,
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


def LogsData(
    resource_logs: Optional[List[bytes]] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if resource_logs:
        proto_serializer.serialize_repeated_message(b"\n", resource_logs)
    return proto_serializer.out


def ResourceLogs(
    resource: Optional[bytes] = None,
    scope_logs: Optional[List[bytes]] = None,
    schema_url: Optional[str] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if resource is not None:
        proto_serializer.serialize_message(b"\n", resource)
    if scope_logs:
        proto_serializer.serialize_repeated_message(b"\x12", scope_logs)
    if schema_url:
        proto_serializer.serialize_string(b"\x1a", schema_url)
    return proto_serializer.out


def ScopeLogs(
    scope: Optional[bytes] = None,
    log_records: Optional[List[bytes]] = None,
    schema_url: Optional[str] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if scope is not None:
        proto_serializer.serialize_message(b"\n", scope)
    if log_records:
        proto_serializer.serialize_repeated_message(b"\x12", log_records)
    if schema_url:
        proto_serializer.serialize_string(b"\x1a", schema_url)
    return proto_serializer.out


def LogRecord(
    time_unix_nano: Optional[int] = None,
    severity_number: Optional[int] = None,
    severity_text: Optional[str] = None,
    body: Optional[bytes] = None,
    attributes: Optional[List[bytes]] = None,
    dropped_attributes_count: Optional[int] = None,
    flags: Optional[int] = None,
    trace_id: Optional[bytes] = None,
    span_id: Optional[bytes] = None,
    observed_time_unix_nano: Optional[int] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if time_unix_nano:
        proto_serializer.serialize_fixed64(b"\t", time_unix_nano)
    if severity_number:
        proto_serializer.serialize_enum(b"\x10", severity_number)
    if severity_text:
        proto_serializer.serialize_string(b"\x1a", severity_text)
    if body is not None:
        proto_serializer.serialize_message(b"*", body)
    if attributes:
        proto_serializer.serialize_repeated_message(b"2", attributes)
    if dropped_attributes_count:
        proto_serializer.serialize_uint32(b"8", dropped_attributes_count)
    if flags:
        proto_serializer.serialize_fixed32(b"E", flags)
    if trace_id:
        proto_serializer.serialize_bytes(b"J", trace_id)
    if span_id:
        proto_serializer.serialize_bytes(b"R", span_id)
    if observed_time_unix_nano:
        proto_serializer.serialize_fixed64(b"Y", observed_time_unix_nano)
    return proto_serializer.out
