# Generated by the protoc compiler with a custom plugin. DO NOT EDIT!
# sources: opentelemetry/proto/common/v1/common.proto

from __future__ import annotations

from typing import (
    List,
    Optional,
)

from snowflake.telemetry._internal.serialize import (
    Enum,
    MessageMarshaler,
    ProtoSerializer,
    util,
)


class AnyValue(MessageMarshaler):
    def __init__(
        self,
        string_value: str = None,
        bool_value: bool = None,
        int_value: int = None,
        double_value: float = None,
        array_value: ArrayValue = None,
        kvlist_value: KeyValueList = None,
        bytes_value: bytes = None,
    ):
        self.string_value: str = string_value
        self.bool_value: bool = bool_value
        self.int_value: int = int_value
        self.double_value: float = double_value
        self.array_value: ArrayValue = array_value
        self.kvlist_value: KeyValueList = kvlist_value
        self.bytes_value: bytes = bytes_value
        super().__init__()

    def calculate_size(self) -> int:
        size = 0
        if self.string_value is not None:  # oneof group value
            size += util.size_string(b"\n", self.string_value)
        if self.bool_value is not None:  # oneof group value
            size += util.size_bool(b"\x10", self.bool_value)
        if self.int_value is not None:  # oneof group value
            size += util.size_int64(b"\x18", self.int_value)
        if self.double_value is not None:  # oneof group value
            size += util.size_double(b"!", self.double_value)
        if self.array_value is not None:  # oneof group value
            size += util.size_message(b"*", self.array_value)
        if self.kvlist_value is not None:  # oneof group value
            size += util.size_message(b"2", self.kvlist_value)
        if self.bytes_value is not None:  # oneof group value
            size += util.size_bytes(b":", self.bytes_value)
        return size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.string_value is not None:  # oneof group value
            proto_serializer.serialize_string(b"\n", self.string_value)
        if self.bool_value is not None:  # oneof group value
            proto_serializer.serialize_bool(b"\x10", self.bool_value)
        if self.int_value is not None:  # oneof group value
            proto_serializer.serialize_int64(b"\x18", self.int_value)
        if self.double_value is not None:  # oneof group value
            proto_serializer.serialize_double(b"!", self.double_value)
        if self.array_value is not None:  # oneof group value
            proto_serializer.serialize_message(b"*", self.array_value)
        if self.kvlist_value is not None:  # oneof group value
            proto_serializer.serialize_message(b"2", self.kvlist_value)
        if self.bytes_value is not None:  # oneof group value
            proto_serializer.serialize_bytes(b":", self.bytes_value)


class ArrayValue(MessageMarshaler):
    def __init__(
        self,
        values: List[AnyValue] = None,
    ):
        self.values: List[AnyValue] = values
        super().__init__()

    def calculate_size(self) -> int:
        size = 0
        if self.values:
            size += util.size_repeated_message(b"\n", self.values)
        return size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.values:
            proto_serializer.serialize_repeated_message(b"\n", self.values)


class KeyValueList(MessageMarshaler):
    def __init__(
        self,
        values: List[KeyValue] = None,
    ):
        self.values: List[KeyValue] = values
        super().__init__()

    def calculate_size(self) -> int:
        size = 0
        if self.values:
            size += util.size_repeated_message(b"\n", self.values)
        return size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.values:
            proto_serializer.serialize_repeated_message(b"\n", self.values)


class KeyValue(MessageMarshaler):
    def __init__(
        self,
        key: str = "",
        value: AnyValue = None,
    ):
        self.key: str = key
        self.value: AnyValue = value
        super().__init__()

    def calculate_size(self) -> int:
        size = 0
        if self.key:
            size += util.size_string(b"\n", self.key)
        if self.value is not None:
            size += util.size_message(b"\x12", self.value)
        return size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.key:
            proto_serializer.serialize_string(b"\n", self.key)
        if self.value is not None:
            proto_serializer.serialize_message(b"\x12", self.value)


class InstrumentationScope(MessageMarshaler):
    def __init__(
        self,
        name: str = "",
        version: str = "",
        attributes: List[KeyValue] = None,
        dropped_attributes_count: int = 0,
    ):
        self.name: str = name
        self.version: str = version
        self.attributes: List[KeyValue] = attributes
        self.dropped_attributes_count: int = dropped_attributes_count
        super().__init__()

    def calculate_size(self) -> int:
        size = 0
        if self.name:
            size += util.size_string(b"\n", self.name)
        if self.version:
            size += util.size_string(b"\x12", self.version)
        if self.attributes:
            size += util.size_repeated_message(b"\x1a", self.attributes)
        if self.dropped_attributes_count:
            size += util.size_uint32(b" ", self.dropped_attributes_count)
        return size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.name:
            proto_serializer.serialize_string(b"\n", self.name)
        if self.version:
            proto_serializer.serialize_string(b"\x12", self.version)
        if self.attributes:
            proto_serializer.serialize_repeated_message(b"\x1a", self.attributes)
        if self.dropped_attributes_count:
            proto_serializer.serialize_uint32(b" ", self.dropped_attributes_count)