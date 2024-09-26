# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources:
# plugin: python-serialize

from typing import List

from snowflake.telemetry.serialize import (
    Enum,
    MessageMarshaler,
    ProtoSerializer,
)


class Resource(MessageMarshaler):
    def __init__(
        self,
        attributes: List[MessageMarshaler] = None,
        dropped_attributes_count: int = 0,
    ):
        self.attributes = attributes
        self.dropped_attributes_count = dropped_attributes_count

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.dropped_attributes_count:
            proto_serializer.serialize_uint32(b"\x10", self.dropped_attributes_count)
        if self.attributes:
            proto_serializer.serialize_repeated_message(b"\n", self.attributes)
