try:
    from opentelemetry.exporter.otlp.proto.common.version import __version__ as opentelemetry_proto_version
    from snowflake.telemetry._internal.opentelemetry.exporter.otlp.proto.common.version import __version__ as snowflake_proto_version
    if opentelemetry_proto_version != snowflake_proto_version:
        raise ImportError(
            f"Incompatible version of opentelemetry-exporter-otlp-proto-common library!"
            f" loaded: {opentelemetry_proto_version}, expected: {snowflake_proto_version}"
        )

    from opentelemetry.exporter.otlp.proto.common._log_encoder import encode_logs
    from opentelemetry.proto.logs.v1.logs_pb2 import LogsData

    from opentelemetry.exporter.otlp.proto.common.metrics_encoder import encode_metrics
    from opentelemetry.proto.metrics.v1.metrics_pb2 import MetricsData

    from opentelemetry.exporter.otlp.proto.common.trace_encoder import encode_spans
    from opentelemetry.proto.trace.v1.trace_pb2 import TracesData

    USING_PROTO = True
except ImportError:
    from snowflake.telemetry._internal.opentelemetry.exporter.otlp.proto.common._log_encoder import encode_logs
    from snowflake.telemetry._internal.opentelemetry.proto.logs.v1.logs import LogsData

    from snowflake.telemetry._internal.opentelemetry.exporter.otlp.proto.common.metrics_encoder import encode_metrics
    from snowflake.telemetry._internal.opentelemetry.proto.metrics.v1.metrics import MetricsData

    from snowflake.telemetry._internal.opentelemetry.exporter.otlp.proto.common.trace_encoder import encode_spans
    from snowflake.telemetry._internal.opentelemetry.proto.trace.v1.trace import TracesData

    USING_PROTO = False

from opentelemetry.sdk._logs import LogData as SDKLogData
from opentelemetry.sdk.metrics.export import MetricsData as SDKMetricsData
from opentelemetry.sdk.trace import ReadableSpan as SDKReadableSpan

from typing import Sequence

def serialize_logs_data(sdk_logs: Sequence[SDKLogData]) -> bytes:
    if USING_PROTO:
        return LogsData(resource_logs=encode_logs(sdk_logs).resource_logs).SerializeToString()
    return bytes(LogsData(resource_logs=encode_logs(sdk_logs).resource_logs))

def serialize_metrics_data(sdk_metrics: SDKMetricsData) -> bytes:
    if USING_PROTO:
        return MetricsData(resource_metrics=encode_metrics(sdk_metrics).resource_metrics).SerializeToString()
    return bytes(MetricsData(resource_metrics=encode_metrics(sdk_metrics).resource_metrics))

def serialize_traces_data(sdk_spans: Sequence[SDKReadableSpan]) -> bytes:
    if USING_PROTO:
        return TracesData(resource_spans=encode_spans(sdk_spans).resource_spans).SerializeToString()
    return bytes(TracesData(resource_spans=encode_spans(sdk_spans).resource_spans))
