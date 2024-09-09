from dataclasses import dataclass
from typing import List

import serialize

from opentelemetry.proto.trace.v1 import trace_pb2


@dataclass
class ExportTraceServiceRequest(serialize.Message):
    resource_spans: List[trace_pb2.ResourceSpans] = serialize.message_field(1)


@dataclass
class ExportTraceServiceResponse(serialize.Message):
    partial_success: "ExportTracePartialSuccess" = serialize.message_field(1)


@dataclass
class ExportTracePartialSuccess(serialize.Message):
    rejected_spans: int = serialize.int64_field(1)
    error_message: str = serialize.string_field(2)
