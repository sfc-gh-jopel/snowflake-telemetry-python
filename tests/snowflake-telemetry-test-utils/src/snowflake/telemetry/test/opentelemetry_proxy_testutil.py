from unittest import mock
import importlib
import snowflake.telemetry._internal.opentelemetry_proxy

def reload_opentelemetry_proxy(use_otel=False):
    if use_otel:
        with mock.patch('opentelemetry.exporter.otlp.proto.common.version.__version__', side_effect=ImportError):
            importlib.reload(snowflake.telemetry._internal.opentelemetry_proxy)
        assert not snowflake.telemetry._internal.opentelemetry_proxy.USING_PROTO
    else:
        importlib.reload(snowflake.telemetry._internal.opentelemetry_proxy)
        assert snowflake.telemetry._internal.opentelemetry_proxy.USING_PROTO
