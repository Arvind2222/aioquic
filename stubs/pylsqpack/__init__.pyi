from typing import List, Tuple

Headers = List[Tuple[bytes, bytes]]

class Decoder:
    def __init__(self, max_table_capacity: int, blocked_streams: int) -> None: ...
    def feed_header(self, stream_id: int, data: bytes) -> Tuple[bytes, Headers]: ...

class Encoder:
    def apply_settings(
        self, max_table_capacity: int, blocked_streams: int
    ) -> bytes: ...
    def encode(
        self, stream_id: int, seqno: int, headers: Headers
    ) -> Tuple[bytes, bytes]: ...