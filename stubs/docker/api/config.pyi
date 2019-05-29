"""Stubs for docker.api.config."""

from typing import Dict, Optional, Union

class ConfigApiMixin:
    def create_config(
            self,
            name: str,
            data: Union[str, bytes],
            labels: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]: ...

    def inspect_config(self, id: str) -> Dict[str, str]: ...
    def remove_config(self, id: str) -> bool: ...
    def configs(self, filters: Optional[Dict[str, str]] = None) -> Dict[str, str]: ...
