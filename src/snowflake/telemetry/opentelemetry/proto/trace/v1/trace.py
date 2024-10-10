# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources:
# plugin: python-serialize

from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from snowflake.telemetry.serialize import (
    Enum,
    ProtoSerializer,
    util,
)


class SpanFlags(Enum):
    SPAN_FLAGS_DO_NOT_USE = 0
    SPAN_FLAGS_TRACE_FLAGS_MASK = 255
    SPAN_FLAGS_CONTEXT_HAS_IS_REMOTE_MASK = 256
    SPAN_FLAGS_CONTEXT_IS_REMOTE_MASK = 512


def TracesData(
    resource_spans: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    size = 0
    if resource_spans:
        size += util.size_repeated_message(b"\n", resource_spans)

    return {
        "__size": size,
        "__serialize_function": write_to_TracesData,
        "resource_spans": resource_spans,
    }


def write_to_TracesData(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["resource_spans"]:
        proto_serializer.serialize_repeated_message(b"\n", message["resource_spans"])


def ResourceSpans(
    resource: Optional[Dict[str, Any]] = None,
    scope_spans: Optional[List[Dict[str, Any]]] = None,
    schema_url: Optional[str] = None,
) -> Dict[str, Any]:
    size = 0
    if resource:
        size += util.size_message(b"\n", resource)
    if scope_spans:
        size += util.size_repeated_message(b"\x12", scope_spans)
    if schema_url:
        size += util.size_string(b"\x1a", schema_url)

    return {
        "__size": size,
        "__serialize_function": write_to_ResourceSpans,
        "resource": resource,
        "scope_spans": scope_spans,
        "schema_url": schema_url,
    }


def write_to_ResourceSpans(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["resource"]:
        proto_serializer.serialize_message(b"\n", message["resource"])
    if message["scope_spans"]:
        proto_serializer.serialize_repeated_message(b"\x12", message["scope_spans"])
    if message["schema_url"]:
        proto_serializer.serialize_string(b"\x1a", message["schema_url"])


def ScopeSpans(
    scope: Optional[Dict[str, Any]] = None,
    spans: Optional[List[Dict[str, Any]]] = None,
    schema_url: Optional[str] = None,
) -> Dict[str, Any]:
    size = 0
    if scope:
        size += util.size_message(b"\n", scope)
    if spans:
        size += util.size_repeated_message(b"\x12", spans)
    if schema_url:
        size += util.size_string(b"\x1a", schema_url)

    return {
        "__size": size,
        "__serialize_function": write_to_ScopeSpans,
        "scope": scope,
        "spans": spans,
        "schema_url": schema_url,
    }


def write_to_ScopeSpans(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["scope"]:
        proto_serializer.serialize_message(b"\n", message["scope"])
    if message["spans"]:
        proto_serializer.serialize_repeated_message(b"\x12", message["spans"])
    if message["schema_url"]:
        proto_serializer.serialize_string(b"\x1a", message["schema_url"])


def Span(
    trace_id: Optional[bytes] = None,
    span_id: Optional[bytes] = None,
    trace_state: Optional[str] = None,
    parent_span_id: Optional[bytes] = None,
    name: Optional[str] = None,
    kind: Optional[int] = None,
    start_time_unix_nano: Optional[int] = None,
    end_time_unix_nano: Optional[int] = None,
    attributes: Optional[List[Dict[str, Any]]] = None,
    dropped_attributes_count: Optional[int] = None,
    events: Optional[List[Dict[str, Any]]] = None,
    dropped_events_count: Optional[int] = None,
    links: Optional[List[Dict[str, Any]]] = None,
    dropped_links_count: Optional[int] = None,
    status: Optional[Dict[str, Any]] = None,
    flags: Optional[int] = None,
) -> Dict[str, Any]:
    size = 0
    if trace_id:
        size += util.size_bytes(b"\n", trace_id)
    if span_id:
        size += util.size_bytes(b"\x12", span_id)
    if trace_state:
        size += util.size_string(b"\x1a", trace_state)
    if parent_span_id:
        size += util.size_bytes(b'"', parent_span_id)
    if name:
        size += util.size_string(b"*", name)
    if kind:
        size += util.size_enum(b"0", kind)
    if start_time_unix_nano:
        size += util.size_fixed64(b"9", start_time_unix_nano)
    if end_time_unix_nano:
        size += util.size_fixed64(b"A", end_time_unix_nano)
    if attributes:
        size += util.size_repeated_message(b"J", attributes)
    if dropped_attributes_count:
        size += util.size_uint32(b"P", dropped_attributes_count)
    if events:
        size += util.size_repeated_message(b"Z", events)
    if dropped_events_count:
        size += util.size_uint32(b"`", dropped_events_count)
    if links:
        size += util.size_repeated_message(b"j", links)
    if dropped_links_count:
        size += util.size_uint32(b"p", dropped_links_count)
    if status:
        size += util.size_message(b"z", status)
    if flags:
        size += util.size_fixed32(b"\x85\x01", flags)

    return {
        "__size": size,
        "__serialize_function": write_to_Span,
        "trace_id": trace_id,
        "span_id": span_id,
        "trace_state": trace_state,
        "parent_span_id": parent_span_id,
        "name": name,
        "kind": kind,
        "start_time_unix_nano": start_time_unix_nano,
        "end_time_unix_nano": end_time_unix_nano,
        "attributes": attributes,
        "dropped_attributes_count": dropped_attributes_count,
        "events": events,
        "dropped_events_count": dropped_events_count,
        "links": links,
        "dropped_links_count": dropped_links_count,
        "status": status,
        "flags": flags,
    }


def write_to_Span(message: Dict[str, Any], proto_serializer: ProtoSerializer) -> None:
    if message["trace_id"]:
        proto_serializer.serialize_bytes(b"\n", message["trace_id"])
    if message["span_id"]:
        proto_serializer.serialize_bytes(b"\x12", message["span_id"])
    if message["trace_state"]:
        proto_serializer.serialize_string(b"\x1a", message["trace_state"])
    if message["parent_span_id"]:
        proto_serializer.serialize_bytes(b'"', message["parent_span_id"])
    if message["name"]:
        proto_serializer.serialize_string(b"*", message["name"])
    if message["kind"]:
        proto_serializer.serialize_enum(b"0", message["kind"])
    if message["start_time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"9", message["start_time_unix_nano"])
    if message["end_time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"A", message["end_time_unix_nano"])
    if message["attributes"]:
        proto_serializer.serialize_repeated_message(b"J", message["attributes"])
    if message["dropped_attributes_count"]:
        proto_serializer.serialize_uint32(b"P", message["dropped_attributes_count"])
    if message["events"]:
        proto_serializer.serialize_repeated_message(b"Z", message["events"])
    if message["dropped_events_count"]:
        proto_serializer.serialize_uint32(b"`", message["dropped_events_count"])
    if message["links"]:
        proto_serializer.serialize_repeated_message(b"j", message["links"])
    if message["dropped_links_count"]:
        proto_serializer.serialize_uint32(b"p", message["dropped_links_count"])
    if message["status"]:
        proto_serializer.serialize_message(b"z", message["status"])
    if message["flags"]:
        proto_serializer.serialize_fixed32(b"\x85\x01", message["flags"])


def Status(
    message: Optional[str] = None,
    code: Optional[int] = None,
) -> Dict[str, Any]:
    size = 0
    if message:
        size += util.size_string(b"\x12", message)
    if code:
        size += util.size_enum(b"\x18", code)

    return {
        "__size": size,
        "__serialize_function": write_to_Status,
        "message": message,
        "code": code,
    }


def write_to_Status(message: Dict[str, Any], proto_serializer: ProtoSerializer) -> None:
    if message["message"]:
        proto_serializer.serialize_string(b"\x12", message["message"])
    if message["code"]:
        proto_serializer.serialize_enum(b"\x18", message["code"])
