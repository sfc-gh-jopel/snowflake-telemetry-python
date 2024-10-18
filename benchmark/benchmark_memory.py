from benchmark.util import get_logs_data
from snowflake.telemetry._internal.exporter.otlp.proto.logs import encode_logs


"""
v0.5.0

📦 Total memory allocated: 19.9KiB
📏 Total allocations: 19
📊 Histogram of allocation sizes: |█▁▂ ▁|
🥇 Biggest allocating functions:
    - _encode_log:/Users/jopel/workspace/snowflake-telemetry-python/.venv/lib/python3.11/site-packages/opentelemetry/exporter/otlp/proto/common/_internal/_log_encoder/__init__.py:52 -> 6.4KiB
    - _encode_resource_logs:/Users/jopel/workspace/snowflake-telemetry-python/.venv/lib/python3.11/site-packages/opentelemetry/exporter/otlp/proto/common/_internal/_log_encoder/__init__.py:88 -> 5.7KiB
    - _encode_resource_logs:/Users/jopel/workspace/snowflake-telemetry-python/.venv/lib/python3.11/site-packages/opentelemetry/exporter/otlp/proto/common/_internal/_log_encoder/__init__.py:82 -> 3.5KiB
    - __setitem__:/Users/jopel/workspace/snowflake-telemetry-python/.venv/lib/python3.11/site-packages/opentelemetry/attributes/__init__.py:173 -> 804.0B
"""

"""
v0.6.0.dev

📦 Total memory allocated: 4.9KiB
📏 Total allocations: 18
📊 Histogram of allocation sizes: |█   ▄|
🥇 Biggest allocating functions:
    - __setitem__:/home/jopel/workspace/snowflake-telemetry-python/.venv/lib/python3.11/site-packages/opentelemetry/attributes/__init__.py:173 -> 804.0B
    - encode_logs:/home/jopel/workspace/snowflake-telemetry-python/.venv/lib/python3.11/site-packages/snowflake/telemetry/_internal/opentelemetry/exporter/otlp/proto/common/_internal/_log_encoder/__init__.py:38 -> 723.0B
    - serialize_message:/home/jopel/workspace/snowflake-telemetry-python/.venv/lib/python3.11/site-packages/snowflake/telemetry/_internal/serialize/__init__.py:95 -> 691.0B
    - _encode_log:/home/jopel/workspace/snowflake-telemetry-python/.venv/lib/python3.11/site-packages/snowflake/telemetry/_internal/opentelemetry/exporter/otlp/proto/common/_internal/_log_encoder/__init__.py:58 -> 646.0B
"""

# Run with pytest --memray tests/benchmark_memory.py
def test_serialize_logs():
    logs_data = get_logs_data()
    bytes(encode_logs(logs_data))
