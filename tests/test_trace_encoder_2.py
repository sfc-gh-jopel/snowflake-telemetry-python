import importlib
import test_trace_encoder
import snowflake.telemetry._internal.exporter.otlp.proto.traces
from snowflake.telemetry.test.opentelemetry_proxy_test_utils import reload_module

class TestOTLPTraceEncoder(test_trace_encoder.TestOTLPTraceEncoder):
    def setUp(self):
        reload_module(use_custom=False)
        importlib.reload(snowflake.telemetry._internal.exporter.otlp.proto.traces)
        importlib.reload(test_trace_encoder)

class TestOTLPTraceEncoderCustom(test_trace_encoder.TestOTLPTraceEncoder):
    def setUp(self):
        reload_module(use_custom=True)
        importlib.reload(snowflake.telemetry._internal.exporter.otlp.proto.traces)
        importlib.reload(test_trace_encoder)
