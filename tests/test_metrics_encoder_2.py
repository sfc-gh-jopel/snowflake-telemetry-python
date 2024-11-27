import importlib
import test_metrics_encoder
import snowflake.telemetry._internal.exporter.otlp.proto.metrics
from snowflake.telemetry.test.opentelemetry_proxy_test_utils import reload_module

class TestOTLPMetricsEncoder(test_metrics_encoder.TestOTLPMetricsEncoder):
    def setUp(self):
        reload_module(use_custom=False)
        importlib.reload(snowflake.telemetry._internal.exporter.otlp.proto.metrics)
        importlib.reload(test_metrics_encoder)

class TestOTLPMetricsEncoderCustom(test_metrics_encoder.TestOTLPMetricsEncoder):
    def setUp(self):
        reload_module(use_custom=True)
        importlib.reload(snowflake.telemetry._internal.exporter.otlp.proto.metrics)
        importlib.reload(test_metrics_encoder)