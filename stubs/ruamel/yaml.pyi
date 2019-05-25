"""Type stubs for ruamel.yaml."""

from typing import Dict, IO, Union

class YAML:

    def load(self, pointer: IO[str]) -> Dict[str, Union[str, int, float]]: ...