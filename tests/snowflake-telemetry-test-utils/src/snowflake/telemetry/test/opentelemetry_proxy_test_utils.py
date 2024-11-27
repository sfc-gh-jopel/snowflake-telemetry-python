import importlib
import snowflake.telemetry._internal.opentelemetry_proxy

from unittest import mock

def assert_module(obj, expected_module):
    assert obj.__module__.startswith(expected_module)

def reload_module(use_custom: bool):
    if use_custom:
        # Inject ImportError to simulate missing opentelemetry-exporter-otlp-proto-common library
        with mock.patch("opentelemetry.exporter.otlp.proto.common.version.__version__", side_effect=ImportError):
            importlib.reload(snowflake.telemetry._internal.opentelemetry_proxy)
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.encode_logs, "snowflake.telemetry._internal.opentelemetry.exporter.otlp.proto.common._internal._log_encoder")
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.LogsData, "snowflake.telemetry._internal.opentelemetry.proto.logs.v1.logs_marshaler")
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.encode_metrics, "snowflake.telemetry._internal.opentelemetry.exporter.otlp.proto.common._internal.metrics_encoder")
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.MetricsData, "snowflake.telemetry._internal.opentelemetry.proto.metrics.v1.metrics_marshaler")
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.encode_spans, "snowflake.telemetry._internal.opentelemetry.exporter.otlp.proto.common._internal.trace_encoder")
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.TracesData, "snowflake.telemetry._internal.opentelemetry.proto.trace.v1.trace_marshaler")
    else:
        importlib.reload(snowflake.telemetry._internal.opentelemetry_proxy)
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.encode_logs, "opentelemetry.exporter.otlp.proto.common._internal._log_encoder")
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.LogsData, "opentelemetry.proto.logs.v1.logs_pb2")
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.encode_metrics, "opentelemetry.exporter.otlp.proto.common._internal.metrics_encoder")
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.MetricsData, "opentelemetry.proto.metrics.v1.metrics_pb2")
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.encode_spans, "opentelemetry.exporter.otlp.proto.common._internal.trace_encoder")
        assert_module(snowflake.telemetry._internal.opentelemetry_proxy.TracesData, "opentelemetry.proto.trace.v1.trace_pb2")        
