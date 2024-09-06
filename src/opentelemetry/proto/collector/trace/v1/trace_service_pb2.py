# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: opentelemetry/proto/collector/trace/v1/trace_service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto
import grpclib

from opentelemetry.proto.trace.v1 import trace_pb2 as v1


@dataclass
class ExportTraceServiceRequest(betterproto.Message):
    # An array of ResourceSpans. For data coming from a single resource this
    # array will typically contain one element. Intermediary nodes (such as
    # OpenTelemetry Collector) that receive data from multiple origins typically
    # batch the data before forwarding further and in that case this array will
    # contain multiple elements.
    resource_spans: List[v1.ResourceSpans] = betterproto.message_field(1)


@dataclass
class ExportTraceServiceResponse(betterproto.Message):
    # The details of a partially successful export request. If the request is
    # only partially accepted (i.e. when the server accepts only parts of the
    # data and rejects the rest) the server MUST initialize the `partial_success`
    # field and MUST set the `rejected_<signal>` with the number of items it
    # rejected. Servers MAY also make use of the `partial_success` field to
    # convey warnings/suggestions to senders even when the request was fully
    # accepted. In such cases, the `rejected_<signal>` MUST have a value of `0`
    # and the `error_message` MUST be non-empty. A `partial_success` message with
    # an empty value (rejected_<signal> = 0 and `error_message` = "") is
    # equivalent to it not being set/present. Senders SHOULD interpret it the
    # same way as in the full success case.
    partial_success: "ExportTracePartialSuccess" = betterproto.message_field(1)


@dataclass
class ExportTracePartialSuccess(betterproto.Message):
    # The number of rejected spans. A `rejected_<signal>` field holding a `0`
    # value indicates that the request was fully accepted.
    rejected_spans: int = betterproto.int64_field(1)
    # A developer-facing human-readable message in English. It should be used
    # either to explain why the server rejected parts of the data during a
    # partial success or to convey warnings/suggestions during a full success.
    # The message should offer guidance on how users can address such issues.
    # error_message is an optional field. An error_message with an empty value is
    # equivalent to it not being set.
    error_message: str = betterproto.string_field(2)


class TraceServiceStub(betterproto.ServiceStub):
    """
    Service that can be used to push spans between one Application instrumented
    with OpenTelemetry and a collector, or between a collector and a central
    collector (in this case spans are sent/received to/from multiple
    Applications).
    """

    async def export(
        self, *, resource_spans: List[v1.ResourceSpans] = []
    ) -> ExportTraceServiceResponse:
        """
        For performance reasons, it is recommended to keep this RPC alive for
        the entire life of the application.
        """

        request = ExportTraceServiceRequest()
        if resource_spans is not None:
            request.resource_spans = resource_spans

        return await self._unary_unary(
            "/opentelemetry.proto.collector.trace.v1.TraceService/Export",
            request,
            ExportTraceServiceResponse,
        )
