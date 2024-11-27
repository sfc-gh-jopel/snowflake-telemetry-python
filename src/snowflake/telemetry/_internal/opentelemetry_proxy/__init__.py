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
except ImportError as e:
    from snowflake.telemetry._internal.opentelemetry.exporter.otlp.proto.common._log_encoder import encode_logs
    from snowflake.telemetry._internal.opentelemetry.proto.logs.v1.logs_marshaler import LogsData
    from snowflake.telemetry._internal.opentelemetry.exporter.otlp.proto.common.metrics_encoder import encode_metrics
    from snowflake.telemetry._internal.opentelemetry.proto.metrics.v1.metrics_marshaler import MetricsData
    from snowflake.telemetry._internal.opentelemetry.exporter.otlp.proto.common.trace_encoder import encode_spans
    from snowflake.telemetry._internal.opentelemetry.proto.trace.v1.trace_marshaler import TracesData
