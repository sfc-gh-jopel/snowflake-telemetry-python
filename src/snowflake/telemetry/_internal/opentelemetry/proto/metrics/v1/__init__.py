# Generated by the protoc compiler with a custom plugin. DO NOT EDIT!
# sources: opentelemetry/proto/metrics/v1/metrics.proto

from __future__ import annotations

import struct
from io import BytesIO
from typing import (
    List,
    Optional,
)

from snowflake.telemetry._internal.opentelemetry.proto.common.v1 import *
from snowflake.telemetry._internal.opentelemetry.proto.resource.v1 import *
from snowflake.telemetry._internal.serialize import (
    Enum,
    MessageMarshaler,
    size_varint32,
    size_varint64,
    write_varint_unsigned,
)


class AggregationTemporality(Enum):
    AGGREGATION_TEMPORALITY_UNSPECIFIED = 0
    AGGREGATION_TEMPORALITY_DELTA = 1
    AGGREGATION_TEMPORALITY_CUMULATIVE = 2


class DataPointFlags(Enum):
    DATA_POINT_FLAGS_DO_NOT_USE = 0
    DATA_POINT_FLAGS_NO_RECORDED_VALUE_MASK = 1


class MetricsData(MessageMarshaler):
    def __init__(
        self,
        resource_metrics: List[ResourceMetrics] = None,
    ):
        self.resource_metrics: List[ResourceMetrics] = resource_metrics

    def calculate_size(self) -> int:
        size = 0
        if self.resource_metrics:
            size += sum(
                message._get_size() + len(b"\n") + size_varint32(message._get_size())
                for message in self.resource_metrics
            )
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.resource_metrics:
            for v in self.resource_metrics:
                out += b"\n"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)


class ResourceMetrics(MessageMarshaler):
    def __init__(
        self,
        resource: Resource = None,
        scope_metrics: List[ScopeMetrics] = None,
        schema_url: str = "",
    ):
        self.resource: Resource = resource
        self.scope_metrics: List[ScopeMetrics] = scope_metrics
        self.schema_url: str = schema_url

    def calculate_size(self) -> int:
        size = 0
        if self.resource is not None:
            size += (
                len(b"\n")
                + size_varint32(self.resource._get_size())
                + self.resource._get_size()
            )
        if self.scope_metrics:
            size += sum(
                message._get_size() + len(b"\x12") + size_varint32(message._get_size())
                for message in self.scope_metrics
            )
        if self.schema_url:
            v = self.schema_url.encode("utf-8")
            self._schema_url_encoded = v
            size += len(b"\x1a") + size_varint32(len(v)) + len(v)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.resource is not None:
            out += b"\n"
            write_varint_unsigned(out, self.resource._get_size())
            self.resource.write_to(out)
        if self.scope_metrics:
            for v in self.scope_metrics:
                out += b"\x12"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.schema_url:
            v = self._schema_url_encoded
            out += b"\x1a"
            write_varint_unsigned(out, len(v))
            out += v


class ScopeMetrics(MessageMarshaler):
    def __init__(
        self,
        scope: InstrumentationScope = None,
        metrics: List[Metric] = None,
        schema_url: str = "",
    ):
        self.scope: InstrumentationScope = scope
        self.metrics: List[Metric] = metrics
        self.schema_url: str = schema_url

    def calculate_size(self) -> int:
        size = 0
        if self.scope is not None:
            size += (
                len(b"\n")
                + size_varint32(self.scope._get_size())
                + self.scope._get_size()
            )
        if self.metrics:
            size += sum(
                message._get_size() + len(b"\x12") + size_varint32(message._get_size())
                for message in self.metrics
            )
        if self.schema_url:
            v = self.schema_url.encode("utf-8")
            self._schema_url_encoded = v
            size += len(b"\x1a") + size_varint32(len(v)) + len(v)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.scope is not None:
            out += b"\n"
            write_varint_unsigned(out, self.scope._get_size())
            self.scope.write_to(out)
        if self.metrics:
            for v in self.metrics:
                out += b"\x12"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.schema_url:
            v = self._schema_url_encoded
            out += b"\x1a"
            write_varint_unsigned(out, len(v))
            out += v


class Metric(MessageMarshaler):
    def __init__(
        self,
        name: str = "",
        description: str = "",
        unit: str = "",
        gauge: Gauge = None,
        sum: Sum = None,
        histogram: Histogram = None,
        exponential_histogram: ExponentialHistogram = None,
        summary: Summary = None,
        metadata: List[KeyValue] = None,
    ):
        self.name: str = name
        self.description: str = description
        self.unit: str = unit
        self.gauge: Gauge = gauge
        self.sum: Sum = sum
        self.histogram: Histogram = histogram
        self.exponential_histogram: ExponentialHistogram = exponential_histogram
        self.summary: Summary = summary
        self.metadata: List[KeyValue] = metadata

    def calculate_size(self) -> int:
        size = 0
        if self.name:
            v = self.name.encode("utf-8")
            self._name_encoded = v
            size += len(b"\n") + size_varint32(len(v)) + len(v)
        if self.description:
            v = self.description.encode("utf-8")
            self._description_encoded = v
            size += len(b"\x12") + size_varint32(len(v)) + len(v)
        if self.unit:
            v = self.unit.encode("utf-8")
            self._unit_encoded = v
            size += len(b"\x1a") + size_varint32(len(v)) + len(v)
        if self.gauge is not None:
            size += (
                len(b"*")
                + size_varint32(self.gauge._get_size())
                + self.gauge._get_size()
            )
        if self.sum is not None:
            size += (
                len(b":") + size_varint32(self.sum._get_size()) + self.sum._get_size()
            )
        if self.histogram is not None:
            size += (
                len(b"J")
                + size_varint32(self.histogram._get_size())
                + self.histogram._get_size()
            )
        if self.exponential_histogram is not None:
            size += (
                len(b"R")
                + size_varint32(self.exponential_histogram._get_size())
                + self.exponential_histogram._get_size()
            )
        if self.summary is not None:
            size += (
                len(b"Z")
                + size_varint32(self.summary._get_size())
                + self.summary._get_size()
            )
        if self.metadata:
            size += sum(
                message._get_size() + len(b"b") + size_varint32(message._get_size())
                for message in self.metadata
            )
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.name:
            v = self._name_encoded
            out += b"\n"
            write_varint_unsigned(out, len(v))
            out += v
        if self.description:
            v = self._description_encoded
            out += b"\x12"
            write_varint_unsigned(out, len(v))
            out += v
        if self.unit:
            v = self._unit_encoded
            out += b"\x1a"
            write_varint_unsigned(out, len(v))
            out += v
        if self.gauge is not None:
            out += b"*"
            write_varint_unsigned(out, self.gauge._get_size())
            self.gauge.write_to(out)
        if self.sum is not None:
            out += b":"
            write_varint_unsigned(out, self.sum._get_size())
            self.sum.write_to(out)
        if self.histogram is not None:
            out += b"J"
            write_varint_unsigned(out, self.histogram._get_size())
            self.histogram.write_to(out)
        if self.exponential_histogram is not None:
            out += b"R"
            write_varint_unsigned(out, self.exponential_histogram._get_size())
            self.exponential_histogram.write_to(out)
        if self.summary is not None:
            out += b"Z"
            write_varint_unsigned(out, self.summary._get_size())
            self.summary.write_to(out)
        if self.metadata:
            for v in self.metadata:
                out += b"b"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)


class Gauge(MessageMarshaler):
    def __init__(
        self,
        data_points: List[NumberDataPoint] = None,
    ):
        self.data_points: List[NumberDataPoint] = data_points

    def calculate_size(self) -> int:
        size = 0
        if self.data_points:
            size += sum(
                message._get_size() + len(b"\n") + size_varint32(message._get_size())
                for message in self.data_points
            )
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.data_points:
            for v in self.data_points:
                out += b"\n"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)


class Sum(MessageMarshaler):
    def __init__(
        self,
        data_points: List[NumberDataPoint] = None,
        aggregation_temporality: int = 0,
        is_monotonic: bool = False,
    ):
        self.data_points: List[NumberDataPoint] = data_points
        self.aggregation_temporality: int = aggregation_temporality
        self.is_monotonic: bool = is_monotonic

    def calculate_size(self) -> int:
        size = 0
        if self.data_points:
            size += sum(
                message._get_size() + len(b"\n") + size_varint32(message._get_size())
                for message in self.data_points
            )
        if self.aggregation_temporality:
            v = self.aggregation_temporality
            if not isinstance(v, int):
                v = v.self.aggregation_temporality
            size += len(b"\x10") + size_varint32(v)
        if self.is_monotonic:
            size += len(b"\x18") + 1
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.data_points:
            for v in self.data_points:
                out += b"\n"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.aggregation_temporality:
            v = self.aggregation_temporality
            if not isinstance(v, int):
                v = v.self.aggregation_temporality
            out += b"\x10"
            write_varint_unsigned(out, v)
        if self.is_monotonic:
            out += b"\x18"
            write_varint_unsigned(out, 1 if self.is_monotonic else 0)


class Histogram(MessageMarshaler):
    def __init__(
        self,
        data_points: List[HistogramDataPoint] = None,
        aggregation_temporality: int = 0,
    ):
        self.data_points: List[HistogramDataPoint] = data_points
        self.aggregation_temporality: int = aggregation_temporality

    def calculate_size(self) -> int:
        size = 0
        if self.data_points:
            size += sum(
                message._get_size() + len(b"\n") + size_varint32(message._get_size())
                for message in self.data_points
            )
        if self.aggregation_temporality:
            v = self.aggregation_temporality
            if not isinstance(v, int):
                v = v.self.aggregation_temporality
            size += len(b"\x10") + size_varint32(v)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.data_points:
            for v in self.data_points:
                out += b"\n"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.aggregation_temporality:
            v = self.aggregation_temporality
            if not isinstance(v, int):
                v = v.self.aggregation_temporality
            out += b"\x10"
            write_varint_unsigned(out, v)


class ExponentialHistogram(MessageMarshaler):
    def __init__(
        self,
        data_points: List[ExponentialHistogramDataPoint] = None,
        aggregation_temporality: int = 0,
    ):
        self.data_points: List[ExponentialHistogramDataPoint] = data_points
        self.aggregation_temporality: int = aggregation_temporality

    def calculate_size(self) -> int:
        size = 0
        if self.data_points:
            size += sum(
                message._get_size() + len(b"\n") + size_varint32(message._get_size())
                for message in self.data_points
            )
        if self.aggregation_temporality:
            v = self.aggregation_temporality
            if not isinstance(v, int):
                v = v.self.aggregation_temporality
            size += len(b"\x10") + size_varint32(v)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.data_points:
            for v in self.data_points:
                out += b"\n"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.aggregation_temporality:
            v = self.aggregation_temporality
            if not isinstance(v, int):
                v = v.self.aggregation_temporality
            out += b"\x10"
            write_varint_unsigned(out, v)


class Summary(MessageMarshaler):
    def __init__(
        self,
        data_points: List[SummaryDataPoint] = None,
    ):
        self.data_points: List[SummaryDataPoint] = data_points

    def calculate_size(self) -> int:
        size = 0
        if self.data_points:
            size += sum(
                message._get_size() + len(b"\n") + size_varint32(message._get_size())
                for message in self.data_points
            )
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.data_points:
            for v in self.data_points:
                out += b"\n"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)


class NumberDataPoint(MessageMarshaler):
    def __init__(
        self,
        start_time_unix_nano: int = 0,
        time_unix_nano: int = 0,
        as_double: float = None,
        exemplars: List[Exemplar] = None,
        as_int: int = None,
        attributes: List[KeyValue] = None,
        flags: int = 0,
    ):
        self.start_time_unix_nano: int = start_time_unix_nano
        self.time_unix_nano: int = time_unix_nano
        self.as_double: float = as_double
        self.exemplars: List[Exemplar] = exemplars
        self.as_int: int = as_int
        self.attributes: List[KeyValue] = attributes
        self.flags: int = flags

    def calculate_size(self) -> int:
        size = 0
        if self.start_time_unix_nano:
            size += len(b"\x11") + 8
        if self.time_unix_nano:
            size += len(b"\x19") + 8
        if self.as_double is not None:
            size += len(b"!") + 8
        if self.exemplars:
            size += sum(
                message._get_size() + len(b"*") + size_varint32(message._get_size())
                for message in self.exemplars
            )
        if self.as_int is not None:
            size += len(b"1") + 8
        if self.attributes:
            size += sum(
                message._get_size() + len(b":") + size_varint32(message._get_size())
                for message in self.attributes
            )
        if self.flags:
            size += len(b"@") + size_varint32(self.flags)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.start_time_unix_nano:
            out += b"\x11"
            out += struct.pack("<Q", self.start_time_unix_nano)
        if self.time_unix_nano:
            out += b"\x19"
            out += struct.pack("<Q", self.time_unix_nano)
        if self.as_double is not None:
            out += b"!"
            out += struct.pack("<d", self.as_double)
        if self.exemplars:
            for v in self.exemplars:
                out += b"*"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.as_int is not None:
            out += b"1"
            out += struct.pack("<q", self.as_int)
        if self.attributes:
            for v in self.attributes:
                out += b":"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.flags:
            out += b"@"
            write_varint_unsigned(out, self.flags)


class HistogramDataPoint(MessageMarshaler):
    def __init__(
        self,
        start_time_unix_nano: int = 0,
        time_unix_nano: int = 0,
        count: int = 0,
        sum: float = None,
        bucket_counts: List[int] = None,
        explicit_bounds: List[float] = None,
        exemplars: List[Exemplar] = None,
        attributes: List[KeyValue] = None,
        flags: int = 0,
        min: float = None,
        max: float = None,
    ):
        self.start_time_unix_nano: int = start_time_unix_nano
        self.time_unix_nano: int = time_unix_nano
        self.count: int = count
        self.sum: float = sum
        self.bucket_counts: List[int] = bucket_counts
        self.explicit_bounds: List[float] = explicit_bounds
        self.exemplars: List[Exemplar] = exemplars
        self.attributes: List[KeyValue] = attributes
        self.flags: int = flags
        self.min: float = min
        self.max: float = max

    def calculate_size(self) -> int:
        size = 0
        if self.start_time_unix_nano:
            size += len(b"\x11") + 8
        if self.time_unix_nano:
            size += len(b"\x19") + 8
        if self.count:
            size += len(b"!") + 8
        if self.sum is not None:
            size += len(b")") + 8
        if self.bucket_counts:
            size += (
                len(b"2")
                + len(self.bucket_counts) * 8
                + size_varint32(len(self.bucket_counts) * 8)
            )
        if self.explicit_bounds:
            size += (
                len(b":")
                + len(self.explicit_bounds) * 8
                + size_varint32(len(self.explicit_bounds) * 8)
            )
        if self.exemplars:
            size += sum(
                message._get_size() + len(b"B") + size_varint32(message._get_size())
                for message in self.exemplars
            )
        if self.attributes:
            size += sum(
                message._get_size() + len(b"J") + size_varint32(message._get_size())
                for message in self.attributes
            )
        if self.flags:
            size += len(b"P") + size_varint32(self.flags)
        if self.min is not None:
            size += len(b"Y") + 8
        if self.max is not None:
            size += len(b"a") + 8
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.start_time_unix_nano:
            out += b"\x11"
            out += struct.pack("<Q", self.start_time_unix_nano)
        if self.time_unix_nano:
            out += b"\x19"
            out += struct.pack("<Q", self.time_unix_nano)
        if self.count:
            out += b"!"
            out += struct.pack("<Q", self.count)
        if self.sum is not None:
            out += b")"
            out += struct.pack("<d", self.sum)
        if self.bucket_counts:
            out += b"2"
            write_varint_unsigned(out, len(self.bucket_counts) * 8)
            for v in self.bucket_counts:
                out += struct.pack("<Q", v)
        if self.explicit_bounds:
            out += b":"
            write_varint_unsigned(out, len(self.explicit_bounds) * 8)
            for v in self.explicit_bounds:
                out += struct.pack("<d", v)
        if self.exemplars:
            for v in self.exemplars:
                out += b"B"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.attributes:
            for v in self.attributes:
                out += b"J"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.flags:
            out += b"P"
            write_varint_unsigned(out, self.flags)
        if self.min is not None:
            out += b"Y"
            out += struct.pack("<d", self.min)
        if self.max is not None:
            out += b"a"
            out += struct.pack("<d", self.max)


class ExponentialHistogramDataPoint(MessageMarshaler):
    def __init__(
        self,
        attributes: List[KeyValue] = None,
        start_time_unix_nano: int = 0,
        time_unix_nano: int = 0,
        count: int = 0,
        sum: float = None,
        scale: int = 0,
        zero_count: int = 0,
        positive: ExponentialHistogramDataPoint.Buckets = None,
        negative: ExponentialHistogramDataPoint.Buckets = None,
        flags: int = 0,
        exemplars: List[Exemplar] = None,
        min: float = None,
        max: float = None,
        zero_threshold: float = 0.0,
    ):
        self.attributes: List[KeyValue] = attributes
        self.start_time_unix_nano: int = start_time_unix_nano
        self.time_unix_nano: int = time_unix_nano
        self.count: int = count
        self.sum: float = sum
        self.scale: int = scale
        self.zero_count: int = zero_count
        self.positive: ExponentialHistogramDataPoint.Buckets = positive
        self.negative: ExponentialHistogramDataPoint.Buckets = negative
        self.flags: int = flags
        self.exemplars: List[Exemplar] = exemplars
        self.min: float = min
        self.max: float = max
        self.zero_threshold: float = zero_threshold

    def calculate_size(self) -> int:
        size = 0
        if self.attributes:
            size += sum(
                message._get_size() + len(b"\n") + size_varint32(message._get_size())
                for message in self.attributes
            )
        if self.start_time_unix_nano:
            size += len(b"\x11") + 8
        if self.time_unix_nano:
            size += len(b"\x19") + 8
        if self.count:
            size += len(b"!") + 8
        if self.sum is not None:
            size += len(b")") + 8
        if self.scale:
            size += len(b"0") + size_varint32(
                self.scale << 1 if self.scale >= 0 else (self.scale << 1) ^ (~0)
            )
        if self.zero_count:
            size += len(b"9") + 8
        if self.positive is not None:
            size += (
                len(b"B")
                + size_varint32(self.positive._get_size())
                + self.positive._get_size()
            )
        if self.negative is not None:
            size += (
                len(b"J")
                + size_varint32(self.negative._get_size())
                + self.negative._get_size()
            )
        if self.flags:
            size += len(b"P") + size_varint32(self.flags)
        if self.exemplars:
            size += sum(
                message._get_size() + len(b"Z") + size_varint32(message._get_size())
                for message in self.exemplars
            )
        if self.min is not None:
            size += len(b"a") + 8
        if self.max is not None:
            size += len(b"i") + 8
        if self.zero_threshold:
            size += len(b"q") + 8
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.attributes:
            for v in self.attributes:
                out += b"\n"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.start_time_unix_nano:
            out += b"\x11"
            out += struct.pack("<Q", self.start_time_unix_nano)
        if self.time_unix_nano:
            out += b"\x19"
            out += struct.pack("<Q", self.time_unix_nano)
        if self.count:
            out += b"!"
            out += struct.pack("<Q", self.count)
        if self.sum is not None:
            out += b")"
            out += struct.pack("<d", self.sum)
        if self.scale:
            out += b"0"
            write_varint_unsigned(
                out, self.scale << 1 if self.scale >= 0 else (self.scale << 1) ^ (~0)
            )
        if self.zero_count:
            out += b"9"
            out += struct.pack("<Q", self.zero_count)
        if self.positive is not None:
            out += b"B"
            write_varint_unsigned(out, self.positive._get_size())
            self.positive.write_to(out)
        if self.negative is not None:
            out += b"J"
            write_varint_unsigned(out, self.negative._get_size())
            self.negative.write_to(out)
        if self.flags:
            out += b"P"
            write_varint_unsigned(out, self.flags)
        if self.exemplars:
            for v in self.exemplars:
                out += b"Z"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.min is not None:
            out += b"a"
            out += struct.pack("<d", self.min)
        if self.max is not None:
            out += b"i"
            out += struct.pack("<d", self.max)
        if self.zero_threshold:
            out += b"q"
            out += struct.pack("<d", self.zero_threshold)

    class Buckets(MessageMarshaler):
        def __init__(
            self,
            offset: int = 0,
            bucket_counts: List[int] = None,
        ):
            self.offset: int = offset
            self.bucket_counts: List[int] = bucket_counts

        def calculate_size(self) -> int:
            size = 0
            if self.offset:
                size += len(b"\x08") + size_varint32(
                    self.offset << 1 if self.offset >= 0 else (self.offset << 1) ^ (~0)
                )
            if self.bucket_counts:
                s = sum(size_varint64(uint32) for uint32 in self.bucket_counts)
                self._bucket_counts_size = s
                size += len(b"\x12") + s + size_varint32(s)
            return size

        def write_to(self, out: BytesIO) -> None:
            if self.offset:
                out += b"\x08"
                write_varint_unsigned(
                    out,
                    self.offset << 1 if self.offset >= 0 else (self.offset << 1) ^ (~0),
                )
            if self.bucket_counts:
                out += b"\x12"
                write_varint_unsigned(out, self._bucket_counts_size)
                for v in self.bucket_counts:
                    write_varint_unsigned(out, v)


class SummaryDataPoint(MessageMarshaler):
    def __init__(
        self,
        start_time_unix_nano: int = 0,
        time_unix_nano: int = 0,
        count: int = 0,
        sum: float = 0.0,
        quantile_values: List[SummaryDataPoint.ValueAtQuantile] = None,
        attributes: List[KeyValue] = None,
        flags: int = 0,
    ):
        self.start_time_unix_nano: int = start_time_unix_nano
        self.time_unix_nano: int = time_unix_nano
        self.count: int = count
        self.sum: float = sum
        self.quantile_values: List[SummaryDataPoint.ValueAtQuantile] = quantile_values
        self.attributes: List[KeyValue] = attributes
        self.flags: int = flags

    def calculate_size(self) -> int:
        size = 0
        if self.start_time_unix_nano:
            size += len(b"\x11") + 8
        if self.time_unix_nano:
            size += len(b"\x19") + 8
        if self.count:
            size += len(b"!") + 8
        if self.sum:
            size += len(b")") + 8
        if self.quantile_values:
            size += sum(
                message._get_size() + len(b"2") + size_varint32(message._get_size())
                for message in self.quantile_values
            )
        if self.attributes:
            size += sum(
                message._get_size() + len(b":") + size_varint32(message._get_size())
                for message in self.attributes
            )
        if self.flags:
            size += len(b"@") + size_varint32(self.flags)
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.start_time_unix_nano:
            out += b"\x11"
            out += struct.pack("<Q", self.start_time_unix_nano)
        if self.time_unix_nano:
            out += b"\x19"
            out += struct.pack("<Q", self.time_unix_nano)
        if self.count:
            out += b"!"
            out += struct.pack("<Q", self.count)
        if self.sum:
            out += b")"
            out += struct.pack("<d", self.sum)
        if self.quantile_values:
            for v in self.quantile_values:
                out += b"2"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.attributes:
            for v in self.attributes:
                out += b":"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
        if self.flags:
            out += b"@"
            write_varint_unsigned(out, self.flags)

    class ValueAtQuantile(MessageMarshaler):
        def __init__(
            self,
            quantile: float = 0.0,
            value: float = 0.0,
        ):
            self.quantile: float = quantile
            self.value: float = value

        def calculate_size(self) -> int:
            size = 0
            if self.quantile:
                size += len(b"\t") + 8
            if self.value:
                size += len(b"\x11") + 8
            return size

        def write_to(self, out: BytesIO) -> None:
            if self.quantile:
                out += b"\t"
                out += struct.pack("<d", self.quantile)
            if self.value:
                out += b"\x11"
                out += struct.pack("<d", self.value)


class Exemplar(MessageMarshaler):
    def __init__(
        self,
        time_unix_nano: int = 0,
        as_double: float = None,
        span_id: bytes = b"",
        trace_id: bytes = b"",
        as_int: int = None,
        filtered_attributes: List[KeyValue] = None,
    ):
        self.time_unix_nano: int = time_unix_nano
        self.as_double: float = as_double
        self.span_id: bytes = span_id
        self.trace_id: bytes = trace_id
        self.as_int: int = as_int
        self.filtered_attributes: List[KeyValue] = filtered_attributes

    def calculate_size(self) -> int:
        size = 0
        if self.time_unix_nano:
            size += len(b"\x11") + 8
        if self.as_double is not None:
            size += len(b"\x19") + 8
        if self.span_id:
            size += len(b'"') + size_varint32(len(self.span_id)) + len(self.span_id)
        if self.trace_id:
            size += len(b"*") + size_varint32(len(self.trace_id)) + len(self.trace_id)
        if self.as_int is not None:
            size += len(b"1") + 8
        if self.filtered_attributes:
            size += sum(
                message._get_size() + len(b":") + size_varint32(message._get_size())
                for message in self.filtered_attributes
            )
        return size

    def write_to(self, out: BytesIO) -> None:
        if self.time_unix_nano:
            out += b"\x11"
            out += struct.pack("<Q", self.time_unix_nano)
        if self.as_double is not None:
            out += b"\x19"
            out += struct.pack("<d", self.as_double)
        if self.span_id:
            out += b'"'
            write_varint_unsigned(out, len(self.span_id))
            out += self.span_id
        if self.trace_id:
            out += b"*"
            write_varint_unsigned(out, len(self.trace_id))
            out += self.trace_id
        if self.as_int is not None:
            out += b"1"
            out += struct.pack("<q", self.as_int)
        if self.filtered_attributes:
            for v in self.filtered_attributes:
                out += b":"
                write_varint_unsigned(out, v._get_size())
                v.write_to(out)
