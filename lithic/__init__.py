# File generated from our OpenAPI spec by Stainless.

from . import types
from ._types import NoneType, Transport, ProxiesTypes
from ._client import (
    ENVIRONMENTS,
    Client,
    Lithic,
    Timeout,
    Transport,
    AsyncClient,
    AsyncLithic,
    ProxiesTypes,
    RequestOptions,
)
from ._version import __title__, __version__
from ._exceptions import (
    APIError,
    ConflictError,
    NotFoundError,
    APIStatusError,
    RateLimitError,
    APITimeoutError,
    BadRequestError,
    APIConnectionError,
    AuthenticationError,
    InternalServerError,
    PermissionDeniedError,
    UnprocessableEntityError,
    APIResponseValidationError,
)

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "APIError",
    "APIConnectionError",
    "APIResponseValidationError",
    "APIStatusError",
    "APITimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "InternalServerError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "UnprocessableEntityError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Lithic",
    "AsyncLithic",
    "ENVIRONMENTS",
]

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# lithic._base_exceptions.NotFoundError -> lithic.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            setattr(__locals[__name], "__module__", "lithic")
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass
