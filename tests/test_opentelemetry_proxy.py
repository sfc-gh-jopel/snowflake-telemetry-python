"""
Tests to ensure the opentelemetry_proxy module is functioning as expected
"""

import unittest
import importlib
from unittest import mock

import snowflake.telemetry._internal.opentelemetry_proxy as opentelemetry_proxy

class TestOpenTelemetryProxy(unittest.TestCase):
    def test_opentelemetry_exporter_otlp_proto_common_present(self):
        importlib.reload(opentelemetry_proxy)
        self.assertTrue(opentelemetry_proxy.USING_PROTO)

    def test_opentelemetry_exporter_otlp_proto_common_not_present(self):
        with mock.patch('opentelemetry.exporter.otlp.proto.common.version.__version__', side_effect=ImportError):
            importlib.reload(opentelemetry_proxy)
            self.assertFalse(opentelemetry_proxy.USING_PROTO)

    def test_opentelemetry_exporter_otlp_proto_common_wrong_version(self):
        with mock.patch('opentelemetry.exporter.otlp.proto.common.version.__version__', '1.0.0'):
            importlib.reload(opentelemetry_proxy)
            self.assertFalse(opentelemetry_proxy.USING_PROTO)
