import importlib
import test_log_encoder
import snowflake.telemetry._internal.exporter.otlp.proto.logs
from snowflake.telemetry.test.opentelemetry_proxy_test_utils import reload_module

class TestOTLPLogEncoder(test_log_encoder.TestOTLPLogEncoder):
    def setUp(self):
        reload_module(use_custom=False)
        importlib.reload(snowflake.telemetry._internal.exporter.otlp.proto.logs)
        importlib.reload(test_log_encoder)

class TestOTLPLogEncoderCustom(test_log_encoder.TestOTLPLogEncoder):
    def setUp(self):
        # reload the opentelemetry_proxy module
        reload_module(use_custom=True)
        # reload the snowflake module
        importlib.reload(snowflake.telemetry._internal.exporter.otlp.proto.logs)
        # reload the test module
        importlib.reload(test_log_encoder)
