from dataclasses import dataclass
from typing import List

import serialize

from snowflake.telemetry.proto.common.v1 import common_pb2


@dataclass
class Resource(serialize.Message):
    attributes: List[common_pb2.KeyValue] = serialize.message_field(1)
    dropped_attributes_count: int = serialize.uint32_field(2)
