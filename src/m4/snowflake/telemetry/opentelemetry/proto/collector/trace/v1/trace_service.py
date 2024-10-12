# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources:
# plugin: python-serialize

from typing import (
    Any,
    Dict,
    List,
    Optional,
    TypedDict,
)

from m4.snowflake.telemetry.serialize import (
    Enum,
    ProtoSerializer,
    util,
)


def ExportTraceServiceRequest(
    resource_spans: Optional[List[bytes]] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if resource_spans:
        proto_serializer.serialize_repeated_message(b"\n", resource_spans)
    return proto_serializer.out


def ExportTraceServiceResponse(
    partial_success: Optional[bytes] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if partial_success:
        proto_serializer.serialize_message(b"\n", partial_success)
    return proto_serializer.out


def ExportTracePartialSuccess(
    rejected_spans: Optional[int] = None,
    error_message: Optional[str] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if rejected_spans:
        proto_serializer.serialize_int64(b"\x08", rejected_spans)
    if error_message:
        proto_serializer.serialize_string(b"\x12", error_message)
    return proto_serializer.out
