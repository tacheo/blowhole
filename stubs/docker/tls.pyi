"""Stubs for docker.tls (Python 3)."""

from typing import Optional, Tuple, Union

class TLSConfig:
    """TLS Configuration."""

    cert: Optional[Tuple[str, str]]
    ca_cert: Optional[str]
    verify: Optional[Union[bool, str]]
    ssl_version: Optional[int]
    assert_hostname: Optional[bool]
    assert_fingerprint: Optional[bool]

    def __init__(
            self,
            client_cert: Optional[Tuple[str, str]] = None,
            ca_cert: Optional[str] = None,
            verify: Optional[Union[bool, str]] = None,
            ssl_version: Optional[int] = None,
            assert_hostname: Optional[bool] = None,
            assert_fingerprint: Optional[bool] = None
    ) -> None: ...

    def configure_client(self, client: 'TLSConfig') -> None: ...
