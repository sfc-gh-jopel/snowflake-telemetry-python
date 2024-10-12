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


def Resource(
    attributes: Optional[List[bytes]] = None,
    dropped_attributes_count: Optional[int] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if attributes:
        proto_serializer.serialize_repeated_message(b"\n", attributes)
    if dropped_attributes_count:
        proto_serializer.serialize_uint32(b"\x10", dropped_attributes_count)
    return proto_serializer.out
