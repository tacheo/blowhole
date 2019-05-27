"""
Type stubs for ruamel.yaml.

ruamel.yaml does have type comments, but they are not very strict.
It does not have a PEP561 marker either, so we can't use them.
"""
from pathlib import Path
from typing import Any, Mapping, Union, IO


Loadable = Union[str, Path, IO[str]]

class YAML:

    def __init__(self, typ: str = 'safe', pure: bool = False): ...

    def load(self, stream: Loadable) -> Mapping[str, Any]: ...