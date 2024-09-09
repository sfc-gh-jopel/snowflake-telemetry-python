from dataclasses import dataclass
from typing import List

import serialize

from opentelemetry.proto.common.v1 import common_pb2
from opentelemetry.proto.resource.v1 import resource_pb2


class AggregationTemporality(serialize.Enum):
    AGGREGATION_TEMPORALITY_UNSPECIFIED = 0
    AGGREGATION_TEMPORALITY_DELTA = 1
    AGGREGATION_TEMPORALITY_CUMULATIVE = 2


class DataPointFlags(serialize.Enum):
    DATA_POINT_FLAGS_DO_NOT_USE = 0
    DATA_POINT_FLAGS_NO_RECORDED_VALUE_MASK = 1


@dataclass
class MetricsData(serialize.Message):
    resource_metrics: List["ResourceMetrics"] = serialize.message_field(1)


@dataclass
class ResourceMetrics(serialize.Message):
    resource: resource_pb2.Resource = serialize.message_field(1)
    scope_metrics: List["ScopeMetrics"] = serialize.message_field(2)
    schema_url: str = serialize.string_field(3)


@dataclass
class ScopeMetrics(serialize.Message):
    scope: common_pb2.InstrumentationScope = serialize.message_field(1)
    metrics: List["Metric"] = serialize.message_field(2)
    schema_url: str = serialize.string_field(3)


@dataclass
class Metric(serialize.Message):
    name: str = serialize.string_field(1)
    description: str = serialize.string_field(2)
    unit: str = serialize.string_field(3)
    gauge: "Gauge" = serialize.message_field(5, group="data")
    sum: "Sum" = serialize.message_field(7, group="data")
    histogram: "Histogram" = serialize.message_field(9, group="data")
    exponential_histogram: "ExponentialHistogram" = serialize.message_field(
        10, group="data"
    )
    summary: "Summary" = serialize.message_field(11, group="data")
    metadata: List[common_pb2.KeyValue] = serialize.message_field(12)


@dataclass
class Gauge(serialize.Message):
    data_points: List["NumberDataPoint"] = serialize.message_field(1)


@dataclass
class Sum(serialize.Message):
    data_points: List["NumberDataPoint"] = serialize.message_field(1)
    aggregation_temporality: "AggregationTemporality" = serialize.enum_field(2)
    is_monotonic: bool = serialize.bool_field(3)


@dataclass
class Histogram(serialize.Message):
    data_points: List["HistogramDataPoint"] = serialize.message_field(1)
    aggregation_temporality: "AggregationTemporality" = serialize.enum_field(2)


@dataclass
class ExponentialHistogram(serialize.Message):
    data_points: List["ExponentialHistogramDataPoint"] = serialize.message_field(1)
    aggregation_temporality: "AggregationTemporality" = serialize.enum_field(2)


@dataclass
class Summary(serialize.Message):
    data_points: List["SummaryDataPoint"] = serialize.message_field(1)


@dataclass
class NumberDataPoint(serialize.Message):
    attributes: List[common_pb2.KeyValue] = serialize.message_field(7)
    start_time_unix_nano: float = serialize.fixed64_field(2)
    time_unix_nano: float = serialize.fixed64_field(3)
    as_double: float = serialize.double_field(4, group="value")
    as_int: float = serialize.sfixed64_field(6, group="value")
    exemplars: List["Exemplar"] = serialize.message_field(5)
    flags: int = serialize.uint32_field(8)


@dataclass
class HistogramDataPoint(serialize.Message):
    attributes: List[common_pb2.KeyValue] = serialize.message_field(9)
    start_time_unix_nano: float = serialize.fixed64_field(2)
    time_unix_nano: float = serialize.fixed64_field(3)
    count: float = serialize.fixed64_field(4)
    sum: float = serialize.double_field(5)
    bucket_counts: List[float] = serialize.fixed64_field(6)
    explicit_bounds: List[float] = serialize.double_field(7)
    exemplars: List["Exemplar"] = serialize.message_field(8)
    flags: int = serialize.uint32_field(10)
    min: float = serialize.double_field(11)
    max: float = serialize.double_field(12)

@dataclass
class ExponentialHistogramDataPoint(serialize.Message):
    attributes: List[common_pb2.KeyValue] = serialize.message_field(1)
    start_time_unix_nano: float = serialize.fixed64_field(2)
    time_unix_nano: float = serialize.fixed64_field(3)
    count: float = serialize.fixed64_field(4)
    sum: float = serialize.double_field(5)
    scale: int = serialize.sint32_field(6)
    zero_count: float = serialize.fixed64_field(7)
    @dataclass
    class Buckets(serialize.Message):
        offset: int = serialize.sint32_field(1)
        bucket_counts: List[int] = serialize.uint64_field(2)
    positive: "Buckets" = serialize.message_field(8)
    negative: "Buckets" = serialize.message_field(9)
    flags: int = serialize.uint32_field(10)
    exemplars: List["Exemplar"] = serialize.message_field(11)
    min: float = serialize.double_field(12)
    max: float = serialize.double_field(13)
    zero_threshold: float = serialize.double_field(14)


@dataclass
class SummaryDataPoint(serialize.Message):
    attributes: List[common_pb2.KeyValue] = serialize.message_field(7)
    start_time_unix_nano: float = serialize.fixed64_field(2)
    time_unix_nano: float = serialize.fixed64_field(3)
    count: float = serialize.fixed64_field(4)
    sum: float = serialize.double_field(5)
    @dataclass
    class ValueAtQuantile(serialize.Message):
        quantile: float = serialize.double_field(1)
        value: float = serialize.double_field(2)
    quantile_values: List["ValueAtQuantile"] = (
        serialize.message_field(6)
    )
    flags: int = serialize.uint32_field(8)


@dataclass
class Exemplar(serialize.Message):
    filtered_attributes: List[common_pb2.KeyValue] = serialize.message_field(7)
    time_unix_nano: float = serialize.fixed64_field(2)
    as_double: float = serialize.double_field(3, group="value")
    as_int: float = serialize.sfixed64_field(6, group="value")
    span_id: bytes = serialize.bytes_field(4)
    trace_id: bytes = serialize.bytes_field(5)
