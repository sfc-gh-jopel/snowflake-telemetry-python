# Generated by the protoc compiler with a custom plugin. DO NOT EDIT!
# sources: opentelemetry/proto/common/v1/common.proto
#
# Copyright (c) 2012-2024 Snowflake Inc. All rights reserved.
#

from snowflake.telemetry._internal.proto_proxy import PROTOBUF_VERSION_MAJOR


if PROTOBUF_VERSION_MAJOR == 3 or PROTOBUF_VERSION_MAJOR == 4:
    from snowflake.telemetry._internal.proto_impl.v3.opentelemetry.proto.common.v1.common_pb2 import *
elif PROTOBUF_VERSION_MAJOR == 5:
    from snowflake.telemetry._internal.proto_impl.v5.opentelemetry.proto.common.v1.common_pb2 import *
else:
    from snowflake.telemetry._internal.proto_impl.py.opentelemetry.proto.common.v1.common_marshaler import *
