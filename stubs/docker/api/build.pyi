"""Typestubs for docker.api.build."""

from ipaddress import IPv4Address, IPv6Address
from logging import Logger
from typing import Dict, Generator, IO, List, Optional, Tuple, Union

log: Logger

class BuildApiMixin:
    def build(self,
              path: Optional[str] = None,
              tag: Optional[str] = None,
              quiet: bool = False,
              fileobj: Optional[IO[str]] = ...,
              nocache: bool = False,
              rm: bool = False,
              timeout: Optional[int] = None,
              custom_context: bool = False,
              encoding: Optional[str] = None,
              pull: bool = False,
              forcerm: bool = False,
              dockerfile: Optional[str] = None,
              container_limits: Optional[Dict[str, Union[str, int]]] = None,
              decode: bool = False,
              buildargs: Optional[Dict[str, str]] = None,  # Unsure about this.
              gzip: bool = False,
              shmsize: Optional[int] = None,
              labels: Optional[Dict[str, str]] = None,  # Unsure about this.
              cache_from: Optional[List[str]] = None,
              target: Optional[str] = None,
              network_mode: Optional[str] = None,
              squash: Optional[bool] = None,
              extra_hosts: Optional[Dict[str, Union[IPv4Address, IPv6Address]]] = None,
              platform: Optional[str] = None,
              isolation: Optional[str] = None,
              use_config_proxy: bool = True,
              ) -> Generator[str]: ...

    def prune_builds(self) -> Dict[str, str]: ...

def process_dockerfile(
        dockerfile: Optional[str],
        path: str
) -> Tuple[Optional[str], Optional[int]]: ...
