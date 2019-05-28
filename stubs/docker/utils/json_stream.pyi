# Stubs for docker.utils.json_stream (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..errors import StreamParseError
from typing import Any, Optional

json_decoder: Any

def stream_as_text(stream: Any) -> None: ...
def json_splitter(buffer: Any): ...
def json_stream(stream: Any): ...
def line_splitter(buffer: Any, separator: str = ...): ...
def split_buffer(stream: Any, splitter: Optional[Any] = ..., decoder: Any = ...): ...