from typing import Sequence

import google_benchmark as benchmark

from snowflake.telemetry.test.metrictestutil import _generate_gauge, _generate_sum

from opentelemetry.exporter.otlp.proto.common._log_encoder import encode_logs as m0_encode_logs
from m1.snowflake.telemetry.opentelemetry.exporter.otlp.proto.common._log_encoder import encode_logs as m1_encode_logs
from m2.snowflake.telemetry.opentelemetry.exporter.otlp.proto.common._log_encoder import encode_logs as m2_encode_logs
from m3.snowflake.telemetry.opentelemetry.exporter.otlp.proto.common._log_encoder import encode_logs as m3_encode_logs
from m4.snowflake.telemetry.opentelemetry.exporter.otlp.proto.common._log_encoder import encode_logs as m4_encode_logs

from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.util.instrumentation import InstrumentationScope

from opentelemetry._logs import SeverityNumber
from opentelemetry.sdk._logs import LogData, LogLimits, LogRecord

from opentelemetry.sdk.metrics.export import (
    AggregationTemporality, 
    Buckets,
    ExponentialHistogram,
    Histogram,
    ExponentialHistogramDataPoint,
    HistogramDataPoint,
    Metric,
    MetricsData,
    ResourceMetrics,
    ScopeMetrics,
)

from opentelemetry.sdk.trace import Event, SpanContext, _Span
from opentelemetry.trace import SpanKind, Link, TraceFlags
from opentelemetry.trace.status import Status, StatusCode

def get_logs_data() -> Sequence[LogData]:
    log1 = LogData(
        log_record=LogRecord(
            timestamp=1644650195189786880,
            observed_timestamp=1644660000000000000,
            trace_id=89564621134313219400156819398935297684,
            span_id=1312458408527513268,
            trace_flags=TraceFlags(0x01),
            severity_text="WARN",
            severity_number=SeverityNumber.WARN,
            body="Do not go gentle into that good night. Rage, rage against the dying of the light",
            resource=Resource(
                {"first_resource": "value"},
                "resource_schema_url",
            ),
            attributes={"a": 1, "b": "c"},
        ),
        instrumentation_scope=InstrumentationScope(
            "first_name", "first_version"
        ),
    )

    log2 = LogData(
        log_record=LogRecord(
            timestamp=1644650249738562048,
            observed_timestamp=1644660000000000000,
            trace_id=0,
            span_id=0,
            trace_flags=TraceFlags.DEFAULT,
            severity_text="WARN",
            severity_number=SeverityNumber.WARN,
            body="Cooper, this is no time for caution!",
            resource=Resource({"second_resource": "CASE"}),
            attributes={},
        ),
        instrumentation_scope=InstrumentationScope(
            "second_name", "second_version"
        ),
    )

    log3 = LogData(
        log_record=LogRecord(
            timestamp=1644650427658989056,
            observed_timestamp=1644660000000000000,
            trace_id=271615924622795969659406376515024083555,
            span_id=4242561578944770265,
            trace_flags=TraceFlags(0x01),
            severity_text="DEBUG",
            severity_number=SeverityNumber.DEBUG,
            body="To our galaxy",
            resource=Resource({"second_resource": "CASE"}),
            attributes={"a": 1, "b": "c"},
        ),
        instrumentation_scope=None,
    )

    log4 = LogData(
        log_record=LogRecord(
            timestamp=1644650584292683008,
            observed_timestamp=1644660000000000000,
            trace_id=212592107417388365804938480559624925555,
            span_id=6077757853989569223,
            trace_flags=TraceFlags(0x01),
            severity_text="INFO",
            severity_number=SeverityNumber.INFO,
            body="Love is the one thing that transcends time and space",
            resource=Resource(
                {"first_resource": "value"},
                "resource_schema_url",
            ),
            attributes={"filename": "model.py", "func_name": "run_method"},
        ),
        instrumentation_scope=InstrumentationScope(
            "another_name", "another_version"
        ),
    )

    return [log1, log2, log3, log4]


HISTOGRAM = Metric(
    name="histogram",
    description="foo",
    unit="s",
    data=Histogram(
        data_points=[
            HistogramDataPoint(
                attributes={"a": 1, "b": True},
                start_time_unix_nano=1641946016139533244,
                time_unix_nano=1641946016139533244,
                count=5,
                sum=67,
                bucket_counts=[1, 4],
                explicit_bounds=[10.0, 20.0],
                min=8,
                max=18,
            )
        ],
        aggregation_temporality=AggregationTemporality.DELTA,
    ),
)


@benchmark.register
def test_bm_m0_serialize_logs_data(state):
    # ORIGINAL
    logs_data = get_logs_data()
    while state:
        m0_encode_logs(logs_data).SerializeToString()

@benchmark.register
def test_bm_m1_serialize_logs_data(state):
    # FORWARD
    logs_data = get_logs_data()
    while state:
        bytes(m1_encode_logs(logs_data))

@benchmark.register
def test_bm_m2_serialize_logs_data(state):
    # BACKWARD
    logs_data = get_logs_data()
    while state:
        bytes(m2_encode_logs(logs_data))

@benchmark.register
def test_bm_m3_serialize_logs_data(state):
    # BACKWARD NO OBJECTS
    logs_data = get_logs_data()
    while state:
        m3_encode_logs(logs_data)

@benchmark.register
def test_bm_m4_serialize_logs_data(state):
    # NAIVE
    logs_data = get_logs_data()
    while state:
        m4_encode_logs(logs_data)

if __name__ == "__main__":
    logs_data = get_logs_data()

    m0 = lambda : m0_encode_logs(logs_data).SerializeToString()
    m1 = lambda : bytes(m1_encode_logs(logs_data))
    m2 = lambda : bytes(m2_encode_logs(logs_data))
    m3 = lambda : m3_encode_logs(logs_data)
    m4 = lambda : m4_encode_logs(logs_data)

    methods = {
        "m0": m0,
        "m1": m1,
        "m2": m2,
        "m3": m3,
        "m4": m4,
    }

    # Sanity check
    for name, lmbda in methods.items():
        if name == "m3":
            continue
        print(f"Checking {name}")
        assert lmbda() == m0()

    # CPU profiling
    import cProfile
    for name, lmbda in methods.items():
        cProfile.runctx(f"for _ in range(1000): {name}()", globals(), locals(), filename=f"{name}_encode_logs.prof")

    # MEMORY profiling
    import tracemalloc
    
    def trace_malloc_func(func, name):
        tracemalloc.start()
        for _ in range(1000):
            func()
        print(f"{name}: (curr, peak)={tracemalloc.get_traced_memory()}; ")
        tracemalloc.stop()
    
    for name, lmbda in methods.items():
        trace_malloc_func(lmbda, f"{name}_encode_logs.prof")
        
    
    # Benchmark
    benchmark.main()
