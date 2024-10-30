# Generated by the protoc compiler with a custom plugin. DO NOT EDIT!
# sources: opentelemetry/proto/metrics/v1/metrics.proto

from typing import (
    List,
    Optional,
)

from snowflake.telemetry._internal.opentelemetry.proto.common.v1 import *
from snowflake.telemetry._internal.opentelemetry.proto.resource.v1 import *
from snowflake.telemetry._internal.serialize import (
    Enum,
    MessageMarshaler,
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


class MetricsData(MessageMarshaler):
    resource_metrics: List["ResourceMetrics"]

    def __init__(
        self,
        resource_metrics=None,
    ):
        self._resource_metrics = resource_metrics
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self._resource_metrics:
            __size += util.size_repeated_message(b"\n", self._resource_metrics)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self._resource_metrics:
            proto_serializer.serialize_repeated_message(b"\n", self._resource_metrics)


class ResourceMetrics(MessageMarshaler):
    resource: "Resource"
    scope_metrics: List["ScopeMetrics"]
    schema_url: str

    def __init__(
        self,
        resource=None,
        scope_metrics=None,
        schema_url="",
    ):
        self._resource = resource
        self._scope_metrics = scope_metrics
        self.schema_url = schema_url
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self._resource is not None:
            __size += util.size_message(b"\n", self._resource)
        if self._scope_metrics:
            __size += util.size_repeated_message(b"\x12", self._scope_metrics)
        if self.schema_url:
            __size += util.size_string(b"\x1a", self.schema_url)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self._resource is not None:
            proto_serializer.serialize_message(b"\n", self._resource)
        if self._scope_metrics:
            proto_serializer.serialize_repeated_message(b"\x12", self._scope_metrics)
        if self.schema_url:
            proto_serializer.serialize_string(b"\x1a", self.schema_url)


class ScopeMetrics(MessageMarshaler):
    scope: "InstrumentationScope"
    metrics: List["Metric"]
    schema_url: str

    def __init__(
        self,
        scope=None,
        metrics=None,
        schema_url="",
    ):
        self._scope = scope
        self._metrics = metrics
        self.schema_url = schema_url
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self._scope is not None:
            __size += util.size_message(b"\n", self._scope)
        if self._metrics:
            __size += util.size_repeated_message(b"\x12", self._metrics)
        if self.schema_url:
            __size += util.size_string(b"\x1a", self.schema_url)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self._scope is not None:
            proto_serializer.serialize_message(b"\n", self._scope)
        if self._metrics:
            proto_serializer.serialize_repeated_message(b"\x12", self._metrics)
        if self.schema_url:
            proto_serializer.serialize_string(b"\x1a", self.schema_url)


class Metric(MessageMarshaler):
    name: str
    description: str
    unit: str
    gauge: "Gauge"
    sum: "Sum"
    histogram: "Histogram"
    exponential_histogram: "ExponentialHistogram"
    summary: "Summary"
    metadata: List["KeyValue"]

    def __init__(
        self,
        name="",
        description="",
        unit="",
        gauge=None,
        sum=None,
        histogram=None,
        exponential_histogram=None,
        summary=None,
        metadata=None,
    ):
        self.name = name
        self.description = description
        self.unit = unit
        self._gauge = gauge
        self._sum = sum
        self._histogram = histogram
        self._exponential_histogram = exponential_histogram
        self._summary = summary
        self._metadata = metadata
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self.name:
            __size += util.size_string(b"\n", self.name)
        if self.description:
            __size += util.size_string(b"\x12", self.description)
        if self.unit:
            __size += util.size_string(b"\x1a", self.unit)
        if self._gauge is not None:  # oneof group data
            __size += util.size_message(b"*", self._gauge)
        if self._sum is not None:  # oneof group data
            __size += util.size_message(b":", self._sum)
        if self._histogram is not None:  # oneof group data
            __size += util.size_message(b"J", self._histogram)
        if self._exponential_histogram is not None:  # oneof group data
            __size += util.size_message(b"R", self._exponential_histogram)
        if self._summary is not None:  # oneof group data
            __size += util.size_message(b"Z", self._summary)
        if self._metadata:
            __size += util.size_repeated_message(b"b", self._metadata)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.name:
            proto_serializer.serialize_string(b"\n", self.name)
        if self.description:
            proto_serializer.serialize_string(b"\x12", self.description)
        if self.unit:
            proto_serializer.serialize_string(b"\x1a", self.unit)
        if self._gauge is not None:  # oneof group data
            proto_serializer.serialize_message(b"*", self._gauge)
        if self._sum is not None:  # oneof group data
            proto_serializer.serialize_message(b":", self._sum)
        if self._histogram is not None:  # oneof group data
            proto_serializer.serialize_message(b"J", self._histogram)
        if self._exponential_histogram is not None:  # oneof group data
            proto_serializer.serialize_message(b"R", self._exponential_histogram)
        if self._summary is not None:  # oneof group data
            proto_serializer.serialize_message(b"Z", self._summary)
        if self._metadata:
            proto_serializer.serialize_repeated_message(b"b", self._metadata)


class Gauge(MessageMarshaler):
    data_points: List["NumberDataPoint"]

    def __init__(
        self,
        data_points=None,
    ):
        self._data_points = data_points
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self._data_points:
            __size += util.size_repeated_message(b"\n", self._data_points)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self._data_points:
            proto_serializer.serialize_repeated_message(b"\n", self._data_points)


class Sum(MessageMarshaler):
    data_points: List["NumberDataPoint"]
    aggregation_temporality: int
    is_monotonic: bool

    def __init__(
        self,
        data_points=None,
        aggregation_temporality=0,
        is_monotonic=False,
    ):
        self._data_points = data_points
        self.aggregation_temporality = aggregation_temporality
        self.is_monotonic = is_monotonic
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self._data_points:
            __size += util.size_repeated_message(b"\n", self._data_points)
        if self.aggregation_temporality:
            __size += util.size_enum(b"\x10", self.aggregation_temporality)
        if self.is_monotonic:
            __size += util.size_bool(b"\x18", self.is_monotonic)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self._data_points:
            proto_serializer.serialize_repeated_message(b"\n", self._data_points)
        if self.aggregation_temporality:
            proto_serializer.serialize_enum(b"\x10", self.aggregation_temporality)
        if self.is_monotonic:
            proto_serializer.serialize_bool(b"\x18", self.is_monotonic)


class Histogram(MessageMarshaler):
    data_points: List["HistogramDataPoint"]
    aggregation_temporality: int

    def __init__(
        self,
        data_points=None,
        aggregation_temporality=0,
    ):
        self._data_points = data_points
        self.aggregation_temporality = aggregation_temporality
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self._data_points:
            __size += util.size_repeated_message(b"\n", self._data_points)
        if self.aggregation_temporality:
            __size += util.size_enum(b"\x10", self.aggregation_temporality)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self._data_points:
            proto_serializer.serialize_repeated_message(b"\n", self._data_points)
        if self.aggregation_temporality:
            proto_serializer.serialize_enum(b"\x10", self.aggregation_temporality)


class ExponentialHistogram(MessageMarshaler):
    data_points: List["ExponentialHistogramDataPoint"]
    aggregation_temporality: int

    def __init__(
        self,
        data_points=None,
        aggregation_temporality=0,
    ):
        self._data_points = data_points
        self.aggregation_temporality = aggregation_temporality
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self._data_points:
            __size += util.size_repeated_message(b"\n", self._data_points)
        if self.aggregation_temporality:
            __size += util.size_enum(b"\x10", self.aggregation_temporality)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self._data_points:
            proto_serializer.serialize_repeated_message(b"\n", self._data_points)
        if self.aggregation_temporality:
            proto_serializer.serialize_enum(b"\x10", self.aggregation_temporality)


class Summary(MessageMarshaler):
    data_points: List["SummaryDataPoint"]

    def __init__(
        self,
        data_points=None,
    ):
        self._data_points = data_points
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self._data_points:
            __size += util.size_repeated_message(b"\n", self._data_points)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self._data_points:
            proto_serializer.serialize_repeated_message(b"\n", self._data_points)


class NumberDataPoint(MessageMarshaler):
    start_time_unix_nano: int
    time_unix_nano: int
    as_double: float
    exemplars: List["Exemplar"]
    as_int: int
    attributes: List["KeyValue"]
    flags: int

    def __init__(
        self,
        start_time_unix_nano=0,
        time_unix_nano=0,
        as_double=None,
        exemplars=None,
        as_int=None,
        attributes=None,
        flags=0,
    ):
        self.start_time_unix_nano = start_time_unix_nano
        self.time_unix_nano = time_unix_nano
        self.as_double = as_double
        self._exemplars = exemplars
        self.as_int = as_int
        self._attributes = attributes
        self.flags = flags
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self.start_time_unix_nano:
            __size += util.size_fixed64(b"\x11", self.start_time_unix_nano)
        if self.time_unix_nano:
            __size += util.size_fixed64(b"\x19", self.time_unix_nano)
        if self.as_double is not None:  # oneof group value
            __size += util.size_double(b"!", self.as_double)
        if self._exemplars:
            __size += util.size_repeated_message(b"*", self._exemplars)
        if self.as_int is not None:  # oneof group value
            __size += util.size_sfixed64(b"1", self.as_int)
        if self._attributes:
            __size += util.size_repeated_message(b":", self._attributes)
        if self.flags:
            __size += util.size_uint32(b"@", self.flags)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.start_time_unix_nano:
            proto_serializer.serialize_fixed64(b"\x11", self.start_time_unix_nano)
        if self.time_unix_nano:
            proto_serializer.serialize_fixed64(b"\x19", self.time_unix_nano)
        if self.as_double is not None:  # oneof group value
            proto_serializer.serialize_double(b"!", self.as_double)
        if self._exemplars:
            proto_serializer.serialize_repeated_message(b"*", self._exemplars)
        if self.as_int is not None:  # oneof group value
            proto_serializer.serialize_sfixed64(b"1", self.as_int)
        if self._attributes:
            proto_serializer.serialize_repeated_message(b":", self._attributes)
        if self.flags:
            proto_serializer.serialize_uint32(b"@", self.flags)


class HistogramDataPoint(MessageMarshaler):
    start_time_unix_nano: int
    time_unix_nano: int
    count: int
    sum: float
    bucket_counts: List[int]
    explicit_bounds: List[float]
    exemplars: List["Exemplar"]
    attributes: List["KeyValue"]
    flags: int
    min: float
    max: float

    def __init__(
        self,
        start_time_unix_nano=0,
        time_unix_nano=0,
        count=0,
        sum=None,
        bucket_counts=None,
        explicit_bounds=None,
        exemplars=None,
        attributes=None,
        flags=0,
        min=None,
        max=None,
    ):
        self.start_time_unix_nano = start_time_unix_nano
        self.time_unix_nano = time_unix_nano
        self.count = count
        self.sum = sum
        self._bucket_counts = bucket_counts
        self._explicit_bounds = explicit_bounds
        self._exemplars = exemplars
        self._attributes = attributes
        self.flags = flags
        self.min = min
        self.max = max
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self.start_time_unix_nano:
            __size += util.size_fixed64(b"\x11", self.start_time_unix_nano)
        if self.time_unix_nano:
            __size += util.size_fixed64(b"\x19", self.time_unix_nano)
        if self.count:
            __size += util.size_fixed64(b"!", self.count)
        if self.sum is not None:  # oneof group _sum
            __size += util.size_double(b")", self.sum)
        if self._bucket_counts:
            __size += util.size_repeated_fixed64(b"2", self._bucket_counts)
        if self._explicit_bounds:
            __size += util.size_repeated_double(b":", self._explicit_bounds)
        if self._exemplars:
            __size += util.size_repeated_message(b"B", self._exemplars)
        if self._attributes:
            __size += util.size_repeated_message(b"J", self._attributes)
        if self.flags:
            __size += util.size_uint32(b"P", self.flags)
        if self.min is not None:  # oneof group _min
            __size += util.size_double(b"Y", self.min)
        if self.max is not None:  # oneof group _max
            __size += util.size_double(b"a", self.max)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.start_time_unix_nano:
            proto_serializer.serialize_fixed64(b"\x11", self.start_time_unix_nano)
        if self.time_unix_nano:
            proto_serializer.serialize_fixed64(b"\x19", self.time_unix_nano)
        if self.count:
            proto_serializer.serialize_fixed64(b"!", self.count)
        if self.sum is not None:  # oneof group _sum
            proto_serializer.serialize_double(b")", self.sum)
        if self._bucket_counts:
            proto_serializer.serialize_repeated_fixed64(b"2", self._bucket_counts)
        if self._explicit_bounds:
            proto_serializer.serialize_repeated_double(b":", self._explicit_bounds)
        if self._exemplars:
            proto_serializer.serialize_repeated_message(b"B", self._exemplars)
        if self._attributes:
            proto_serializer.serialize_repeated_message(b"J", self._attributes)
        if self.flags:
            proto_serializer.serialize_uint32(b"P", self.flags)
        if self.min is not None:  # oneof group _min
            proto_serializer.serialize_double(b"Y", self.min)
        if self.max is not None:  # oneof group _max
            proto_serializer.serialize_double(b"a", self.max)


class ExponentialHistogramDataPoint(MessageMarshaler):
    attributes: List["KeyValue"]
    start_time_unix_nano: int
    time_unix_nano: int
    count: int
    sum: float
    scale: int
    zero_count: int
    positive: "ExponentialHistogramDataPoint.Buckets"
    negative: "ExponentialHistogramDataPoint.Buckets"
    flags: int
    exemplars: List["Exemplar"]
    min: float
    max: float
    zero_threshold: float

    def __init__(
        self,
        attributes=None,
        start_time_unix_nano=0,
        time_unix_nano=0,
        count=0,
        sum=None,
        scale=0,
        zero_count=0,
        positive=None,
        negative=None,
        flags=0,
        exemplars=None,
        min=None,
        max=None,
        zero_threshold=0.0,
    ):
        self._attributes = attributes
        self.start_time_unix_nano = start_time_unix_nano
        self.time_unix_nano = time_unix_nano
        self.count = count
        self.sum = sum
        self.scale = scale
        self.zero_count = zero_count
        self._positive = positive
        self._negative = negative
        self.flags = flags
        self._exemplars = exemplars
        self.min = min
        self.max = max
        self.zero_threshold = zero_threshold
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self._attributes:
            __size += util.size_repeated_message(b"\n", self._attributes)
        if self.start_time_unix_nano:
            __size += util.size_fixed64(b"\x11", self.start_time_unix_nano)
        if self.time_unix_nano:
            __size += util.size_fixed64(b"\x19", self.time_unix_nano)
        if self.count:
            __size += util.size_fixed64(b"!", self.count)
        if self.sum is not None:  # oneof group _sum
            __size += util.size_double(b")", self.sum)
        if self.scale:
            __size += util.size_sint32(b"0", self.scale)
        if self.zero_count:
            __size += util.size_fixed64(b"9", self.zero_count)
        if self._positive is not None:
            __size += util.size_message(b"B", self._positive)
        if self._negative is not None:
            __size += util.size_message(b"J", self._negative)
        if self.flags:
            __size += util.size_uint32(b"P", self.flags)
        if self._exemplars:
            __size += util.size_repeated_message(b"Z", self._exemplars)
        if self.min is not None:  # oneof group _min
            __size += util.size_double(b"a", self.min)
        if self.max is not None:  # oneof group _max
            __size += util.size_double(b"i", self.max)
        if self.zero_threshold:
            __size += util.size_double(b"q", self.zero_threshold)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self._attributes:
            proto_serializer.serialize_repeated_message(b"\n", self._attributes)
        if self.start_time_unix_nano:
            proto_serializer.serialize_fixed64(b"\x11", self.start_time_unix_nano)
        if self.time_unix_nano:
            proto_serializer.serialize_fixed64(b"\x19", self.time_unix_nano)
        if self.count:
            proto_serializer.serialize_fixed64(b"!", self.count)
        if self.sum is not None:  # oneof group _sum
            proto_serializer.serialize_double(b")", self.sum)
        if self.scale:
            proto_serializer.serialize_sint32(b"0", self.scale)
        if self.zero_count:
            proto_serializer.serialize_fixed64(b"9", self.zero_count)
        if self._positive is not None:
            proto_serializer.serialize_message(b"B", self._positive)
        if self._negative is not None:
            proto_serializer.serialize_message(b"J", self._negative)
        if self.flags:
            proto_serializer.serialize_uint32(b"P", self.flags)
        if self._exemplars:
            proto_serializer.serialize_repeated_message(b"Z", self._exemplars)
        if self.min is not None:  # oneof group _min
            proto_serializer.serialize_double(b"a", self.min)
        if self.max is not None:  # oneof group _max
            proto_serializer.serialize_double(b"i", self.max)
        if self.zero_threshold:
            proto_serializer.serialize_double(b"q", self.zero_threshold)

    class Buckets(MessageMarshaler):
        offset: int
        bucket_counts: List[int]

        def __init__(
            self,
            offset=0,
            bucket_counts=None,
        ):
            self.offset = offset
            self._bucket_counts = bucket_counts
            super().__init__()

        def calculate_size(self) -> int:
            __size = 0
            if self.offset:
                __size += util.size_sint32(b"\x08", self.offset)
            if self._bucket_counts:
                __size += util.size_repeated_uint64(b"\x12", self._bucket_counts)
            return __size

        def write_to(self, proto_serializer: ProtoSerializer) -> None:
            if self.offset:
                proto_serializer.serialize_sint32(b"\x08", self.offset)
            if self._bucket_counts:
                proto_serializer.serialize_repeated_uint64(b"\x12", self._bucket_counts)


class SummaryDataPoint(MessageMarshaler):
    start_time_unix_nano: int
    time_unix_nano: int
    count: int
    sum: float
    quantile_values: List["SummaryDataPoint.ValueAtQuantile"]
    attributes: List["KeyValue"]
    flags: int

    def __init__(
        self,
        start_time_unix_nano=0,
        time_unix_nano=0,
        count=0,
        sum=0.0,
        quantile_values=None,
        attributes=None,
        flags=0,
    ):
        self.start_time_unix_nano = start_time_unix_nano
        self.time_unix_nano = time_unix_nano
        self.count = count
        self.sum = sum
        self._quantile_values = quantile_values
        self._attributes = attributes
        self.flags = flags
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self.start_time_unix_nano:
            __size += util.size_fixed64(b"\x11", self.start_time_unix_nano)
        if self.time_unix_nano:
            __size += util.size_fixed64(b"\x19", self.time_unix_nano)
        if self.count:
            __size += util.size_fixed64(b"!", self.count)
        if self.sum:
            __size += util.size_double(b")", self.sum)
        if self._quantile_values:
            __size += util.size_repeated_message(b"2", self._quantile_values)
        if self._attributes:
            __size += util.size_repeated_message(b":", self._attributes)
        if self.flags:
            __size += util.size_uint32(b"@", self.flags)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.start_time_unix_nano:
            proto_serializer.serialize_fixed64(b"\x11", self.start_time_unix_nano)
        if self.time_unix_nano:
            proto_serializer.serialize_fixed64(b"\x19", self.time_unix_nano)
        if self.count:
            proto_serializer.serialize_fixed64(b"!", self.count)
        if self.sum:
            proto_serializer.serialize_double(b")", self.sum)
        if self._quantile_values:
            proto_serializer.serialize_repeated_message(b"2", self._quantile_values)
        if self._attributes:
            proto_serializer.serialize_repeated_message(b":", self._attributes)
        if self.flags:
            proto_serializer.serialize_uint32(b"@", self.flags)

    class ValueAtQuantile(MessageMarshaler):
        quantile: float
        value: float

        def __init__(
            self,
            quantile=0.0,
            value=0.0,
        ):
            self.quantile = quantile
            self.value = value
            super().__init__()

        def calculate_size(self) -> int:
            __size = 0
            if self.quantile:
                __size += util.size_double(b"\t", self.quantile)
            if self.value:
                __size += util.size_double(b"\x11", self.value)
            return __size

        def write_to(self, proto_serializer: ProtoSerializer) -> None:
            if self.quantile:
                proto_serializer.serialize_double(b"\t", self.quantile)
            if self.value:
                proto_serializer.serialize_double(b"\x11", self.value)


class Exemplar(MessageMarshaler):
    time_unix_nano: int
    as_double: float
    span_id: bytes
    trace_id: bytes
    as_int: int
    filtered_attributes: List["KeyValue"]

    def __init__(
        self,
        time_unix_nano=0,
        as_double=None,
        span_id=b"",
        trace_id=b"",
        as_int=None,
        filtered_attributes=None,
    ):
        self.time_unix_nano = time_unix_nano
        self.as_double = as_double
        self.span_id = span_id
        self.trace_id = trace_id
        self.as_int = as_int
        self._filtered_attributes = filtered_attributes
        super().__init__()

    def calculate_size(self) -> int:
        __size = 0
        if self.time_unix_nano:
            __size += util.size_fixed64(b"\x11", self.time_unix_nano)
        if self.as_double is not None:  # oneof group value
            __size += util.size_double(b"\x19", self.as_double)
        if self.span_id:
            __size += util.size_bytes(b'"', self.span_id)
        if self.trace_id:
            __size += util.size_bytes(b"*", self.trace_id)
        if self.as_int is not None:  # oneof group value
            __size += util.size_sfixed64(b"1", self.as_int)
        if self._filtered_attributes:
            __size += util.size_repeated_message(b":", self._filtered_attributes)
        return __size

    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        if self.time_unix_nano:
            proto_serializer.serialize_fixed64(b"\x11", self.time_unix_nano)
        if self.as_double is not None:  # oneof group value
            proto_serializer.serialize_double(b"\x19", self.as_double)
        if self.span_id:
            proto_serializer.serialize_bytes(b'"', self.span_id)
        if self.trace_id:
            proto_serializer.serialize_bytes(b"*", self.trace_id)
        if self.as_int is not None:  # oneof group value
            proto_serializer.serialize_sfixed64(b"1", self.as_int)
        if self._filtered_attributes:
            proto_serializer.serialize_repeated_message(b":", self._filtered_attributes)
