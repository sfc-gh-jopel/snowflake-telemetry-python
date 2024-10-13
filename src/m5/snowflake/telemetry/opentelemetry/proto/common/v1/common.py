# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources:
# plugin: python-serialize

from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from m5.snowflake.telemetry.serialize import (
    Enum,
    ProtoSerializer,
    util,
)


def AnyValue(
    bytes_value: Optional[bytes] = None,
    kvlist_value: Optional[Dict[str, Any]] = None,
    array_value: Optional[Dict[str, Any]] = None,
    double_value: Optional[float] = None,
    int_value: Optional[int] = None,
    bool_value: Optional[bool] = None,
    string_value: Optional[str] = None,
) -> Dict[str, Any]:
    size = 0
    if bytes_value is not None:
        size += util.size_bytes(b":", bytes_value)
    if kvlist_value is not None:
        size += util.size_message(b"2", kvlist_value)
    if array_value is not None:
        size += util.size_message(b"*", array_value)
    if double_value is not None:
        size += util.size_double(b"!", double_value)
    if int_value is not None:
        size += util.size_int64(b"\x18", int_value)
    if bool_value is not None:
        size += util.size_bool(b"\x10", bool_value)
    if string_value is not None:
        size += util.size_string(b"\n", string_value)

    return {
        "__size": size,
        "__serialize_function": write_to_AnyValue,
        "bytes_value": bytes_value,
        "kvlist_value": kvlist_value,
        "array_value": array_value,
        "double_value": double_value,
        "int_value": int_value,
        "bool_value": bool_value,
        "string_value": string_value,
    }


def write_to_AnyValue(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    # oneof group value
    if message["bytes_value"] is not None:
        proto_serializer.serialize_bytes(b":", message["bytes_value"])
    elif message["kvlist_value"] is not None:
        proto_serializer.serialize_message(b"2", message["kvlist_value"])
    elif message["array_value"] is not None:
        proto_serializer.serialize_message(b"*", message["array_value"])
    elif message["double_value"] is not None:
        proto_serializer.serialize_double(b"!", message["double_value"])
    elif message["int_value"] is not None:
        proto_serializer.serialize_int64(b"\x18", message["int_value"])
    elif message["bool_value"] is not None:
        proto_serializer.serialize_bool(b"\x10", message["bool_value"])
    elif message["string_value"] is not None:
        proto_serializer.serialize_string(b"\n", message["string_value"])


def ArrayValue(
    values: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    size = 0
    if values:
        size += util.size_repeated_message(b"\n", values)

    return {
        "__size": size,
        "__serialize_function": write_to_ArrayValue,
        "values": values,
    }


def write_to_ArrayValue(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["values"]:
        proto_serializer.serialize_repeated_message(b"\n", message["values"])


def KeyValueList(
    values: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    size = 0
    if values:
        size += util.size_repeated_message(b"\n", values)

    return {
        "__size": size,
        "__serialize_function": write_to_KeyValueList,
        "values": values,
    }


def write_to_KeyValueList(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["values"]:
        proto_serializer.serialize_repeated_message(b"\n", message["values"])


def KeyValue(
    key: Optional[str] = None,
    value: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    size = 0
    if key:
        size += util.size_string(b"\n", key)
    if value:
        size += util.size_message(b"\x12", value)

    return {
        "__size": size,
        "__serialize_function": write_to_KeyValue,
        "key": key,
        "value": value,
    }


def write_to_KeyValue(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["key"]:
        proto_serializer.serialize_string(b"\n", message["key"])
    if message["value"]:
        proto_serializer.serialize_message(b"\x12", message["value"])


def InstrumentationScope(
    name: Optional[str] = None,
    version: Optional[str] = None,
    attributes: Optional[List[Dict[str, Any]]] = None,
    dropped_attributes_count: Optional[int] = None,
) -> Dict[str, Any]:
    size = 0
    if name:
        size += util.size_string(b"\n", name)
    if version:
        size += util.size_string(b"\x12", version)
    if attributes:
        size += util.size_repeated_message(b"\x1a", attributes)
    if dropped_attributes_count:
        size += util.size_uint32(b" ", dropped_attributes_count)

    return {
        "__size": size,
        "__serialize_function": write_to_InstrumentationScope,
        "name": name,
        "version": version,
        "attributes": attributes,
        "dropped_attributes_count": dropped_attributes_count,
    }


def write_to_InstrumentationScope(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["name"]:
        proto_serializer.serialize_string(b"\n", message["name"])
    if message["version"]:
        proto_serializer.serialize_string(b"\x12", message["version"])
    if message["attributes"]:
        proto_serializer.serialize_repeated_message(b"\x1a", message["attributes"])
    if message["dropped_attributes_count"]:
        proto_serializer.serialize_uint32(b" ", message["dropped_attributes_count"])
