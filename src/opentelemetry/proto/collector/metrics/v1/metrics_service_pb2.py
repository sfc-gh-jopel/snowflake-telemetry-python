from dataclasses import dataclass
from typing import List

import serialize

from opentelemetry.proto.metrics.v1 import metrics_pb2


@dataclass
class ExportMetricsServiceRequest(serialize.Message):
    resource_metrics: List[metrics_pb2.ResourceMetrics] = serialize.message_field(1)


@dataclass
class ExportMetricsServiceResponse(serialize.Message):
    partial_success: "ExportMetricsPartialSuccess" = serialize.message_field(1)


@dataclass
class ExportMetricsPartialSuccess(serialize.Message):
    rejected_data_points: int = serialize.int64_field(1)
    error_message: str = serialize.string_field(2)
