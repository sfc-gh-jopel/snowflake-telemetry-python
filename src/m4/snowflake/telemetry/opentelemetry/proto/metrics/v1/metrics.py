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


class AggregationTemporality(Enum):
    AGGREGATION_TEMPORALITY_UNSPECIFIED = 0
    AGGREGATION_TEMPORALITY_DELTA = 1
    AGGREGATION_TEMPORALITY_CUMULATIVE = 2


class DataPointFlags(Enum):
    DATA_POINT_FLAGS_DO_NOT_USE = 0
    DATA_POINT_FLAGS_NO_RECORDED_VALUE_MASK = 1


def MetricsData(
    resource_metrics: Optional[List[bytes]] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if resource_metrics:
        proto_serializer.serialize_repeated_message(b"\n", resource_metrics)
    return proto_serializer.out


def ResourceMetrics(
    resource: Optional[bytes] = None,
    scope_metrics: Optional[List[bytes]] = None,
    schema_url: Optional[str] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if resource:
        proto_serializer.serialize_message(b"\n", resource)
    if scope_metrics:
        proto_serializer.serialize_repeated_message(b"\x12", scope_metrics)
    if schema_url:
        proto_serializer.serialize_string(b"\x1a", schema_url)
    return proto_serializer.out


def ScopeMetrics(
    scope: Optional[bytes] = None,
    metrics: Optional[List[bytes]] = None,
    schema_url: Optional[str] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if scope:
        proto_serializer.serialize_message(b"\n", scope)
    if metrics:
        proto_serializer.serialize_repeated_message(b"\x12", metrics)
    if schema_url:
        proto_serializer.serialize_string(b"\x1a", schema_url)
    return proto_serializer.out


def Metric(
    name: Optional[str] = None,
    description: Optional[str] = None,
    unit: Optional[str] = None,
    summary: Optional[bytes] = None,
    exponential_histogram: Optional[bytes] = None,
    histogram: Optional[bytes] = None,
    sum: Optional[bytes] = None,
    gauge: Optional[bytes] = None,
    metadata: Optional[List[bytes]] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if name:
        proto_serializer.serialize_string(b"\n", name)
    if description:
        proto_serializer.serialize_string(b"\x12", description)
    if unit:
        proto_serializer.serialize_string(b"\x1a", unit)
    # oneof group data
    if summary is not None:
        proto_serializer.serialize_message(b"Z", summary)
    elif exponential_histogram is not None:
        proto_serializer.serialize_message(b"R", exponential_histogram)
    elif histogram is not None:
        proto_serializer.serialize_message(b"J", histogram)
    elif sum is not None:
        proto_serializer.serialize_message(b":", sum)
    elif gauge is not None:
        proto_serializer.serialize_message(b"*", gauge)
    if metadata:
        proto_serializer.serialize_repeated_message(b"b", metadata)
    return proto_serializer.out


def Gauge(
    data_points: Optional[List[bytes]] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if data_points:
        proto_serializer.serialize_repeated_message(b"\n", data_points)
    return proto_serializer.out


def Sum(
    data_points: Optional[List[bytes]] = None,
    aggregation_temporality: Optional[int] = None,
    is_monotonic: Optional[bool] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if data_points:
        proto_serializer.serialize_repeated_message(b"\n", data_points)
    if aggregation_temporality:
        proto_serializer.serialize_enum(b"\x10", aggregation_temporality)
    if is_monotonic:
        proto_serializer.serialize_bool(b"\x18", is_monotonic)
    return proto_serializer.out


def Histogram(
    data_points: Optional[List[bytes]] = None,
    aggregation_temporality: Optional[int] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if data_points:
        proto_serializer.serialize_repeated_message(b"\n", data_points)
    if aggregation_temporality:
        proto_serializer.serialize_enum(b"\x10", aggregation_temporality)
    return proto_serializer.out


def ExponentialHistogram(
    data_points: Optional[List[bytes]] = None,
    aggregation_temporality: Optional[int] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if data_points:
        proto_serializer.serialize_repeated_message(b"\n", data_points)
    if aggregation_temporality:
        proto_serializer.serialize_enum(b"\x10", aggregation_temporality)
    return proto_serializer.out


def Summary(
    data_points: Optional[List[bytes]] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if data_points:
        proto_serializer.serialize_repeated_message(b"\n", data_points)
    return proto_serializer.out


def NumberDataPoint(
    start_time_unix_nano: Optional[int] = None,
    time_unix_nano: Optional[int] = None,
    exemplars: Optional[List[bytes]] = None,
    as_int: Optional[int] = None,
    as_double: Optional[float] = None,
    attributes: Optional[List[bytes]] = None,
    flags: Optional[int] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if start_time_unix_nano:
        proto_serializer.serialize_fixed64(b"\x11", start_time_unix_nano)
    if time_unix_nano:
        proto_serializer.serialize_fixed64(b"\x19", time_unix_nano)
    if exemplars:
        proto_serializer.serialize_repeated_message(b"*", exemplars)
    # oneof group value
    if as_int is not None:
        proto_serializer.serialize_sfixed64(b"1", as_int)
    elif as_double is not None:
        proto_serializer.serialize_double(b"!", as_double)
    if attributes:
        proto_serializer.serialize_repeated_message(b":", attributes)
    if flags:
        proto_serializer.serialize_uint32(b"@", flags)
    return proto_serializer.out


def HistogramDataPoint(
    start_time_unix_nano: Optional[int] = None,
    time_unix_nano: Optional[int] = None,
    count: Optional[int] = None,
    sum: Optional[float] = None,
    bucket_counts: Optional[List[int]] = None,
    explicit_bounds: Optional[List[float]] = None,
    exemplars: Optional[List[bytes]] = None,
    attributes: Optional[List[bytes]] = None,
    flags: Optional[int] = None,
    min: Optional[float] = None,
    max: Optional[float] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if start_time_unix_nano:
        proto_serializer.serialize_fixed64(b"\x11", start_time_unix_nano)
    if time_unix_nano:
        proto_serializer.serialize_fixed64(b"\x19", time_unix_nano)
    if count:
        proto_serializer.serialize_fixed64(b"!", count)
    # oneof group _sum
    if sum is not None:
        proto_serializer.serialize_double(b")", sum)
    if bucket_counts:
        proto_serializer.serialize_repeated_fixed64(b"2", bucket_counts)
    if explicit_bounds:
        proto_serializer.serialize_repeated_double(b":", explicit_bounds)
    if exemplars:
        proto_serializer.serialize_repeated_message(b"B", exemplars)
    if attributes:
        proto_serializer.serialize_repeated_message(b"J", attributes)
    if flags:
        proto_serializer.serialize_uint32(b"P", flags)
    # oneof group _min
    if min is not None:
        proto_serializer.serialize_double(b"Y", min)
    # oneof group _max
    if max is not None:
        proto_serializer.serialize_double(b"a", max)
    return proto_serializer.out


def ExponentialHistogramDataPoint(
    attributes: Optional[List[bytes]] = None,
    start_time_unix_nano: Optional[int] = None,
    time_unix_nano: Optional[int] = None,
    count: Optional[int] = None,
    sum: Optional[float] = None,
    scale: Optional[int] = None,
    zero_count: Optional[int] = None,
    positive: Optional[bytes] = None,
    negative: Optional[bytes] = None,
    flags: Optional[int] = None,
    exemplars: Optional[List[bytes]] = None,
    min: Optional[float] = None,
    max: Optional[float] = None,
    zero_threshold: Optional[float] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if attributes:
        proto_serializer.serialize_repeated_message(b"\n", attributes)
    if start_time_unix_nano:
        proto_serializer.serialize_fixed64(b"\x11", start_time_unix_nano)
    if time_unix_nano:
        proto_serializer.serialize_fixed64(b"\x19", time_unix_nano)
    if count:
        proto_serializer.serialize_fixed64(b"!", count)
    # oneof group _sum
    if sum is not None:
        proto_serializer.serialize_double(b")", sum)
    if scale:
        proto_serializer.serialize_sint32(b"0", scale)
    if zero_count:
        proto_serializer.serialize_fixed64(b"9", zero_count)
    if positive:
        proto_serializer.serialize_message(b"B", positive)
    if negative:
        proto_serializer.serialize_message(b"J", negative)
    if flags:
        proto_serializer.serialize_uint32(b"P", flags)
    if exemplars:
        proto_serializer.serialize_repeated_message(b"Z", exemplars)
    # oneof group _min
    if min is not None:
        proto_serializer.serialize_double(b"a", min)
    # oneof group _max
    if max is not None:
        proto_serializer.serialize_double(b"i", max)
    if zero_threshold:
        proto_serializer.serialize_double(b"q", zero_threshold)
    return proto_serializer.out


def SummaryDataPoint(
    start_time_unix_nano: Optional[int] = None,
    time_unix_nano: Optional[int] = None,
    count: Optional[int] = None,
    sum: Optional[float] = None,
    quantile_values: Optional[List[bytes]] = None,
    attributes: Optional[List[bytes]] = None,
    flags: Optional[int] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if start_time_unix_nano:
        proto_serializer.serialize_fixed64(b"\x11", start_time_unix_nano)
    if time_unix_nano:
        proto_serializer.serialize_fixed64(b"\x19", time_unix_nano)
    if count:
        proto_serializer.serialize_fixed64(b"!", count)
    if sum:
        proto_serializer.serialize_double(b")", sum)
    if quantile_values:
        proto_serializer.serialize_repeated_message(b"2", quantile_values)
    if attributes:
        proto_serializer.serialize_repeated_message(b":", attributes)
    if flags:
        proto_serializer.serialize_uint32(b"@", flags)
    return proto_serializer.out


def Exemplar(
    time_unix_nano: Optional[int] = None,
    span_id: Optional[bytes] = None,
    trace_id: Optional[bytes] = None,
    as_int: Optional[int] = None,
    as_double: Optional[float] = None,
    filtered_attributes: Optional[List[bytes]] = None,
) -> bytes:
    proto_serializer = ProtoSerializer()
    if time_unix_nano:
        proto_serializer.serialize_fixed64(b"\x11", time_unix_nano)
    if span_id:
        proto_serializer.serialize_bytes(b'"', span_id)
    if trace_id:
        proto_serializer.serialize_bytes(b"*", trace_id)
    # oneof group value
    if as_int is not None:
        proto_serializer.serialize_sfixed64(b"1", as_int)
    elif as_double is not None:
        proto_serializer.serialize_double(b"\x19", as_double)
    if filtered_attributes:
        proto_serializer.serialize_repeated_message(b":", filtered_attributes)
    return proto_serializer.out