"""Typestubs for docker.api.client."""

import requests.exceptions
from ..constants import DEFAULT_TIMEOUT_SECONDS, DEFAULT_USER_AGENT
from .build import BuildApiMixin
from .config import ConfigApiMixin
from .container import ContainerApiMixin
from .daemon import DaemonApiMixin
from .exec_api import ExecApiMixin
from .image import ImageApiMixin
from .network import NetworkApiMixin
from .plugin import PluginApiMixin
from .secret import SecretApiMixin
from .service import ServiceApiMixin
from .swarm import SwarmApiMixin
from .volume import VolumeApiMixin
from typing import Optional

class APIClient(
    requests.Session,
    BuildApiMixin,
    ConfigApiMixin,
    ContainerApiMixin,
    DaemonApiMixin,
    ExecApiMixin,
    ImageApiMixin,
    NetworkApiMixin,
    PluginApiMixin,
    SecretApiMixin,
    ServiceApiMixin,
    SwarmApiMixin,
    VolumeApiMixin,
):
    # __attrs__: Any
    base_url: str
    timeout: int
    # credstore_env: Any = ...
    def __init__(self,
                 base_url: Optional[str] = None,
                 version: Optional[str] = None,
                 timeout: int = DEFAULT_TIMEOUT_SECONDS,
                 tls: bool = False,
                 user_agent: str = DEFAULT_USER_AGENT,
                 num_pools: Optional[int] = ...,
                 # credstore_env: Optional[Any] = ...
                 ) -> None: ...

    @property
    def api_version(self) -> Optional[str]: ...

    def get_adapter(self, url: str) -> requests.adapters.BaseAdapter: ...
    def reload_config(self, dockercfg_path: Optional[str] = None) -> None: ...
