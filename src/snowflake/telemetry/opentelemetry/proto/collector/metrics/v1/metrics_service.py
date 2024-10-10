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

from snowflake.telemetry.serialize import (
    Enum,
    ProtoSerializer,
    util,
)


def ExportMetricsServiceRequest(
    resource_metrics: Optional[List[bytes]] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if resource_metrics:
        proto_serializer.serialize_repeated_message(b"\n", resource_metrics)
    return proto_serializer.out


def ExportMetricsServiceResponse(
    partial_success: Optional[bytes] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if partial_success:
        proto_serializer.serialize_message(b"\n", partial_success)
    return proto_serializer.out


def ExportMetricsPartialSuccess(
    rejected_data_points: Optional[int] = None,
    error_message: Optional[str] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if rejected_data_points:
        proto_serializer.serialize_int64(b"\x08", rejected_data_points)
    if error_message:
        proto_serializer.serialize_string(b"\x12", error_message)
    return proto_serializer.out
