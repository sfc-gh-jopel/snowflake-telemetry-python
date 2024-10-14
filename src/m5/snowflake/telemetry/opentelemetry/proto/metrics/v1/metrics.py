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


class AggregationTemporality(Enum):
    AGGREGATION_TEMPORALITY_UNSPECIFIED = 0
    AGGREGATION_TEMPORALITY_DELTA = 1
    AGGREGATION_TEMPORALITY_CUMULATIVE = 2


class DataPointFlags(Enum):
    DATA_POINT_FLAGS_DO_NOT_USE = 0
    DATA_POINT_FLAGS_NO_RECORDED_VALUE_MASK = 1


def MetricsData(
    resource_metrics: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    size = 0
    if resource_metrics:
        size += util.size_repeated_message(b"\n", resource_metrics)

    return {
        "__size": size,
        "__serialize_function": write_to_MetricsData,
        "resource_metrics": resource_metrics,
    }


def write_to_MetricsData(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["resource_metrics"]:
        proto_serializer.serialize_repeated_message(b"\n", message["resource_metrics"])


def ResourceMetrics(
    resource: Optional[Dict[str, Any]] = None,
    scope_metrics: Optional[List[Dict[str, Any]]] = None,
    schema_url: Optional[str] = None,
) -> Dict[str, Any]:
    size = 0
    if resource:
        size += util.size_message(b"\n", resource)
    if scope_metrics:
        size += util.size_repeated_message(b"\x12", scope_metrics)
    if schema_url:
        size += util.size_string(b"\x1a", schema_url)

    return {
        "__size": size,
        "__serialize_function": write_to_ResourceMetrics,
        "resource": resource,
        "scope_metrics": scope_metrics,
        "schema_url": schema_url,
    }


def write_to_ResourceMetrics(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["resource"]:
        proto_serializer.serialize_message(b"\n", message["resource"])
    if message["scope_metrics"]:
        proto_serializer.serialize_repeated_message(b"\x12", message["scope_metrics"])
    if message["schema_url"]:
        proto_serializer.serialize_string(b"\x1a", message["schema_url"])


def ScopeMetrics(
    scope: Optional[Dict[str, Any]] = None,
    metrics: Optional[List[Dict[str, Any]]] = None,
    schema_url: Optional[str] = None,
) -> Dict[str, Any]:
    size = 0
    if scope:
        size += util.size_message(b"\n", scope)
    if metrics:
        size += util.size_repeated_message(b"\x12", metrics)
    if schema_url:
        size += util.size_string(b"\x1a", schema_url)

    return {
        "__size": size,
        "__serialize_function": write_to_ScopeMetrics,
        "scope": scope,
        "metrics": metrics,
        "schema_url": schema_url,
    }


def write_to_ScopeMetrics(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["scope"]:
        proto_serializer.serialize_message(b"\n", message["scope"])
    if message["metrics"]:
        proto_serializer.serialize_repeated_message(b"\x12", message["metrics"])
    if message["schema_url"]:
        proto_serializer.serialize_string(b"\x1a", message["schema_url"])


def Metric(
    name: Optional[str] = None,
    description: Optional[str] = None,
    unit: Optional[str] = None,
    summary: Optional[Dict[str, Any]] = None,
    exponential_histogram: Optional[Dict[str, Any]] = None,
    histogram: Optional[Dict[str, Any]] = None,
    sum: Optional[Dict[str, Any]] = None,
    gauge: Optional[Dict[str, Any]] = None,
    metadata: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    size = 0
    if name:
        size += util.size_string(b"\n", name)
    if description:
        size += util.size_string(b"\x12", description)
    if unit:
        size += util.size_string(b"\x1a", unit)
    if summary is not None:
        size += util.size_message(b"Z", summary)
    if exponential_histogram is not None:
        size += util.size_message(b"R", exponential_histogram)
    if histogram is not None:
        size += util.size_message(b"J", histogram)
    if sum is not None:
        size += util.size_message(b":", sum)
    if gauge is not None:
        size += util.size_message(b"*", gauge)
    if metadata:
        size += util.size_repeated_message(b"b", metadata)

    return {
        "__size": size,
        "__serialize_function": write_to_Metric,
        "name": name,
        "description": description,
        "unit": unit,
        "summary": summary,
        "exponential_histogram": exponential_histogram,
        "histogram": histogram,
        "sum": sum,
        "gauge": gauge,
        "metadata": metadata,
    }


def write_to_Metric(message: Dict[str, Any], proto_serializer: ProtoSerializer) -> None:
    if message["name"]:
        proto_serializer.serialize_string(b"\n", message["name"])
    if message["description"]:
        proto_serializer.serialize_string(b"\x12", message["description"])
    if message["unit"]:
        proto_serializer.serialize_string(b"\x1a", message["unit"])
    # oneof group data
    if message["summary"] is not None:
        proto_serializer.serialize_message(b"Z", message["summary"])
    elif message["exponential_histogram"] is not None:
        proto_serializer.serialize_message(b"R", message["exponential_histogram"])
    elif message["histogram"] is not None:
        proto_serializer.serialize_message(b"J", message["histogram"])
    elif message["sum"] is not None:
        proto_serializer.serialize_message(b":", message["sum"])
    elif message["gauge"] is not None:
        proto_serializer.serialize_message(b"*", message["gauge"])
    if message["metadata"]:
        proto_serializer.serialize_repeated_message(b"b", message["metadata"])


def Gauge(
    data_points: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    size = 0
    if data_points:
        size += util.size_repeated_message(b"\n", data_points)

    return {
        "__size": size,
        "__serialize_function": write_to_Gauge,
        "data_points": data_points,
    }


def write_to_Gauge(message: Dict[str, Any], proto_serializer: ProtoSerializer) -> None:
    if message["data_points"]:
        proto_serializer.serialize_repeated_message(b"\n", message["data_points"])


def Sum(
    data_points: Optional[List[Dict[str, Any]]] = None,
    aggregation_temporality: Optional[int] = None,
    is_monotonic: Optional[bool] = None,
) -> Dict[str, Any]:
    size = 0
    if data_points:
        size += util.size_repeated_message(b"\n", data_points)
    if aggregation_temporality:
        size += util.size_enum(b"\x10", aggregation_temporality)
    if is_monotonic:
        size += util.size_bool(b"\x18", is_monotonic)

    return {
        "__size": size,
        "__serialize_function": write_to_Sum,
        "data_points": data_points,
        "aggregation_temporality": aggregation_temporality,
        "is_monotonic": is_monotonic,
    }


def write_to_Sum(message: Dict[str, Any], proto_serializer: ProtoSerializer) -> None:
    if message["data_points"]:
        proto_serializer.serialize_repeated_message(b"\n", message["data_points"])
    if message["aggregation_temporality"]:
        proto_serializer.serialize_enum(b"\x10", message["aggregation_temporality"])
    if message["is_monotonic"]:
        proto_serializer.serialize_bool(b"\x18", message["is_monotonic"])


def Histogram(
    data_points: Optional[List[Dict[str, Any]]] = None,
    aggregation_temporality: Optional[int] = None,
) -> Dict[str, Any]:
    size = 0
    if data_points:
        size += util.size_repeated_message(b"\n", data_points)
    if aggregation_temporality:
        size += util.size_enum(b"\x10", aggregation_temporality)

    return {
        "__size": size,
        "__serialize_function": write_to_Histogram,
        "data_points": data_points,
        "aggregation_temporality": aggregation_temporality,
    }


def write_to_Histogram(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["data_points"]:
        proto_serializer.serialize_repeated_message(b"\n", message["data_points"])
    if message["aggregation_temporality"]:
        proto_serializer.serialize_enum(b"\x10", message["aggregation_temporality"])


def ExponentialHistogram(
    data_points: Optional[List[Dict[str, Any]]] = None,
    aggregation_temporality: Optional[int] = None,
) -> Dict[str, Any]:
    size = 0
    if data_points:
        size += util.size_repeated_message(b"\n", data_points)
    if aggregation_temporality:
        size += util.size_enum(b"\x10", aggregation_temporality)

    return {
        "__size": size,
        "__serialize_function": write_to_ExponentialHistogram,
        "data_points": data_points,
        "aggregation_temporality": aggregation_temporality,
    }


def write_to_ExponentialHistogram(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["data_points"]:
        proto_serializer.serialize_repeated_message(b"\n", message["data_points"])
    if message["aggregation_temporality"]:
        proto_serializer.serialize_enum(b"\x10", message["aggregation_temporality"])


def Summary(
    data_points: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    size = 0
    if data_points:
        size += util.size_repeated_message(b"\n", data_points)

    return {
        "__size": size,
        "__serialize_function": write_to_Summary,
        "data_points": data_points,
    }


def write_to_Summary(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["data_points"]:
        proto_serializer.serialize_repeated_message(b"\n", message["data_points"])


def NumberDataPoint(
    start_time_unix_nano: Optional[int] = None,
    time_unix_nano: Optional[int] = None,
    exemplars: Optional[List[Dict[str, Any]]] = None,
    as_int: Optional[int] = None,
    as_double: Optional[float] = None,
    attributes: Optional[List[Dict[str, Any]]] = None,
    flags: Optional[int] = None,
) -> Dict[str, Any]:
    size = 0
    if start_time_unix_nano:
        size += util.size_fixed64(b"\x11", start_time_unix_nano)
    if time_unix_nano:
        size += util.size_fixed64(b"\x19", time_unix_nano)
    if exemplars:
        size += util.size_repeated_message(b"*", exemplars)
    if as_int is not None:
        size += util.size_sfixed64(b"1", as_int)
    if as_double is not None:
        size += util.size_double(b"!", as_double)
    if attributes:
        size += util.size_repeated_message(b":", attributes)
    if flags:
        size += util.size_uint32(b"@", flags)

    return {
        "__size": size,
        "__serialize_function": write_to_NumberDataPoint,
        "start_time_unix_nano": start_time_unix_nano,
        "time_unix_nano": time_unix_nano,
        "exemplars": exemplars,
        "as_int": as_int,
        "as_double": as_double,
        "attributes": attributes,
        "flags": flags,
    }


def write_to_NumberDataPoint(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["start_time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"\x11", message["start_time_unix_nano"])
    if message["time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"\x19", message["time_unix_nano"])
    if message["exemplars"]:
        proto_serializer.serialize_repeated_message(b"*", message["exemplars"])
    # oneof group value
    if message["as_int"] is not None:
        proto_serializer.serialize_sfixed64(b"1", message["as_int"])
    elif message["as_double"] is not None:
        proto_serializer.serialize_double(b"!", message["as_double"])
    if message["attributes"]:
        proto_serializer.serialize_repeated_message(b":", message["attributes"])
    if message["flags"]:
        proto_serializer.serialize_uint32(b"@", message["flags"])


def HistogramDataPoint(
    start_time_unix_nano: Optional[int] = None,
    time_unix_nano: Optional[int] = None,
    count: Optional[int] = None,
    sum: Optional[float] = None,
    bucket_counts: Optional[List[int]] = None,
    explicit_bounds: Optional[List[float]] = None,
    exemplars: Optional[List[Dict[str, Any]]] = None,
    attributes: Optional[List[Dict[str, Any]]] = None,
    flags: Optional[int] = None,
    min: Optional[float] = None,
    max: Optional[float] = None,
) -> Dict[str, Any]:
    size = 0
    if start_time_unix_nano:
        size += util.size_fixed64(b"\x11", start_time_unix_nano)
    if time_unix_nano:
        size += util.size_fixed64(b"\x19", time_unix_nano)
    if count:
        size += util.size_fixed64(b"!", count)
    if sum is not None:
        size += util.size_double(b")", sum)
    if bucket_counts:
        size += util.size_repeated_fixed64(b"2", bucket_counts)
    if explicit_bounds:
        size += util.size_repeated_double(b":", explicit_bounds)
    if exemplars:
        size += util.size_repeated_message(b"B", exemplars)
    if attributes:
        size += util.size_repeated_message(b"J", attributes)
    if flags:
        size += util.size_uint32(b"P", flags)
    if min is not None:
        size += util.size_double(b"Y", min)
    if max is not None:
        size += util.size_double(b"a", max)

    return {
        "__size": size,
        "__serialize_function": write_to_HistogramDataPoint,
        "start_time_unix_nano": start_time_unix_nano,
        "time_unix_nano": time_unix_nano,
        "count": count,
        "sum": sum,
        "bucket_counts": bucket_counts,
        "explicit_bounds": explicit_bounds,
        "exemplars": exemplars,
        "attributes": attributes,
        "flags": flags,
        "min": min,
        "max": max,
    }


def write_to_HistogramDataPoint(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["start_time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"\x11", message["start_time_unix_nano"])
    if message["time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"\x19", message["time_unix_nano"])
    if message["count"]:
        proto_serializer.serialize_fixed64(b"!", message["count"])
    # oneof group _sum
    if message["sum"] is not None:
        proto_serializer.serialize_double(b")", message["sum"])
    if message["bucket_counts"]:
        proto_serializer.serialize_repeated_fixed64(b"2", message["bucket_counts"])
    if message["explicit_bounds"]:
        proto_serializer.serialize_repeated_double(b":", message["explicit_bounds"])
    if message["exemplars"]:
        proto_serializer.serialize_repeated_message(b"B", message["exemplars"])
    if message["attributes"]:
        proto_serializer.serialize_repeated_message(b"J", message["attributes"])
    if message["flags"]:
        proto_serializer.serialize_uint32(b"P", message["flags"])
    # oneof group _min
    if message["min"] is not None:
        proto_serializer.serialize_double(b"Y", message["min"])
    # oneof group _max
    if message["max"] is not None:
        proto_serializer.serialize_double(b"a", message["max"])


def ExponentialHistogramDataPoint(
    attributes: Optional[List[Dict[str, Any]]] = None,
    start_time_unix_nano: Optional[int] = None,
    time_unix_nano: Optional[int] = None,
    count: Optional[int] = None,
    sum: Optional[float] = None,
    scale: Optional[int] = None,
    zero_count: Optional[int] = None,
    positive: Optional[Dict[str, Any]] = None,
    negative: Optional[Dict[str, Any]] = None,
    flags: Optional[int] = None,
    exemplars: Optional[List[Dict[str, Any]]] = None,
    min: Optional[float] = None,
    max: Optional[float] = None,
    zero_threshold: Optional[float] = None,
) -> Dict[str, Any]:
    size = 0
    if attributes:
        size += util.size_repeated_message(b"\n", attributes)
    if start_time_unix_nano:
        size += util.size_fixed64(b"\x11", start_time_unix_nano)
    if time_unix_nano:
        size += util.size_fixed64(b"\x19", time_unix_nano)
    if count:
        size += util.size_fixed64(b"!", count)
    if sum is not None:
        size += util.size_double(b")", sum)
    if scale:
        size += util.size_sint32(b"0", scale)
    if zero_count:
        size += util.size_fixed64(b"9", zero_count)
    if positive:
        size += util.size_message(b"B", positive)
    if negative:
        size += util.size_message(b"J", negative)
    if flags:
        size += util.size_uint32(b"P", flags)
    if exemplars:
        size += util.size_repeated_message(b"Z", exemplars)
    if min is not None:
        size += util.size_double(b"a", min)
    if max is not None:
        size += util.size_double(b"i", max)
    if zero_threshold:
        size += util.size_double(b"q", zero_threshold)

    return {
        "__size": size,
        "__serialize_function": write_to_ExponentialHistogramDataPoint,
        "attributes": attributes,
        "start_time_unix_nano": start_time_unix_nano,
        "time_unix_nano": time_unix_nano,
        "count": count,
        "sum": sum,
        "scale": scale,
        "zero_count": zero_count,
        "positive": positive,
        "negative": negative,
        "flags": flags,
        "exemplars": exemplars,
        "min": min,
        "max": max,
        "zero_threshold": zero_threshold,
    }


def write_to_ExponentialHistogramDataPoint(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["attributes"]:
        proto_serializer.serialize_repeated_message(b"\n", message["attributes"])
    if message["start_time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"\x11", message["start_time_unix_nano"])
    if message["time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"\x19", message["time_unix_nano"])
    if message["count"]:
        proto_serializer.serialize_fixed64(b"!", message["count"])
    # oneof group _sum
    if message["sum"] is not None:
        proto_serializer.serialize_double(b")", message["sum"])
    if message["scale"]:
        proto_serializer.serialize_sint32(b"0", message["scale"])
    if message["zero_count"]:
        proto_serializer.serialize_fixed64(b"9", message["zero_count"])
    if message["positive"]:
        proto_serializer.serialize_message(b"B", message["positive"])
    if message["negative"]:
        proto_serializer.serialize_message(b"J", message["negative"])
    if message["flags"]:
        proto_serializer.serialize_uint32(b"P", message["flags"])
    if message["exemplars"]:
        proto_serializer.serialize_repeated_message(b"Z", message["exemplars"])
    # oneof group _min
    if message["min"] is not None:
        proto_serializer.serialize_double(b"a", message["min"])
    # oneof group _max
    if message["max"] is not None:
        proto_serializer.serialize_double(b"i", message["max"])
    if message["zero_threshold"]:
        proto_serializer.serialize_double(b"q", message["zero_threshold"])


def SummaryDataPoint(
    start_time_unix_nano: Optional[int] = None,
    time_unix_nano: Optional[int] = None,
    count: Optional[int] = None,
    sum: Optional[float] = None,
    quantile_values: Optional[List[Dict[str, Any]]] = None,
    attributes: Optional[List[Dict[str, Any]]] = None,
    flags: Optional[int] = None,
) -> Dict[str, Any]:
    size = 0
    if start_time_unix_nano:
        size += util.size_fixed64(b"\x11", start_time_unix_nano)
    if time_unix_nano:
        size += util.size_fixed64(b"\x19", time_unix_nano)
    if count:
        size += util.size_fixed64(b"!", count)
    if sum:
        size += util.size_double(b")", sum)
    if quantile_values:
        size += util.size_repeated_message(b"2", quantile_values)
    if attributes:
        size += util.size_repeated_message(b":", attributes)
    if flags:
        size += util.size_uint32(b"@", flags)

    return {
        "__size": size,
        "__serialize_function": write_to_SummaryDataPoint,
        "start_time_unix_nano": start_time_unix_nano,
        "time_unix_nano": time_unix_nano,
        "count": count,
        "sum": sum,
        "quantile_values": quantile_values,
        "attributes": attributes,
        "flags": flags,
    }


def write_to_SummaryDataPoint(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["start_time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"\x11", message["start_time_unix_nano"])
    if message["time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"\x19", message["time_unix_nano"])
    if message["count"]:
        proto_serializer.serialize_fixed64(b"!", message["count"])
    if message["sum"]:
        proto_serializer.serialize_double(b")", message["sum"])
    if message["quantile_values"]:
        proto_serializer.serialize_repeated_message(b"2", message["quantile_values"])
    if message["attributes"]:
        proto_serializer.serialize_repeated_message(b":", message["attributes"])
    if message["flags"]:
        proto_serializer.serialize_uint32(b"@", message["flags"])


def Exemplar(
    time_unix_nano: Optional[int] = None,
    span_id: Optional[bytes] = None,
    trace_id: Optional[bytes] = None,
    as_int: Optional[int] = None,
    as_double: Optional[float] = None,
    filtered_attributes: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    size = 0
    if time_unix_nano:
        size += util.size_fixed64(b"\x11", time_unix_nano)
    if span_id:
        size += util.size_bytes(b'"', span_id)
    if trace_id:
        size += util.size_bytes(b"*", trace_id)
    if as_int is not None:
        size += util.size_sfixed64(b"1", as_int)
    if as_double is not None:
        size += util.size_double(b"\x19", as_double)
    if filtered_attributes:
        size += util.size_repeated_message(b":", filtered_attributes)

    return {
        "__size": size,
        "__serialize_function": write_to_Exemplar,
        "time_unix_nano": time_unix_nano,
        "span_id": span_id,
        "trace_id": trace_id,
        "as_int": as_int,
        "as_double": as_double,
        "filtered_attributes": filtered_attributes,
    }


def write_to_Exemplar(
    message: Dict[str, Any], proto_serializer: ProtoSerializer
) -> None:
    if message["time_unix_nano"]:
        proto_serializer.serialize_fixed64(b"\x11", message["time_unix_nano"])
    if message["span_id"]:
        proto_serializer.serialize_bytes(b'"', message["span_id"])
    if message["trace_id"]:
        proto_serializer.serialize_bytes(b"*", message["trace_id"])
    # oneof group value
    if message["as_int"] is not None:
        proto_serializer.serialize_sfixed64(b"1", message["as_int"])
    elif message["as_double"] is not None:
        proto_serializer.serialize_double(b"\x19", message["as_double"])
    if message["filtered_attributes"]:
        proto_serializer.serialize_repeated_message(
            b":", message["filtered_attributes"]
        )