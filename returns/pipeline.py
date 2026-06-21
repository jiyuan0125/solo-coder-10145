from typing import Any

from returns._internal.pipeline.flow import flow as flow
from returns._internal.pipeline.managed import managed as managed
from returns._internal.pipeline.pipe import pipe as pipe
from returns.interfaces.unwrappable import Unwrappable
from returns.primitives.exceptions import UnwrapFailedError


def is_successful(container: Unwrappable[Any, Any]) -> bool:
    """
    Determines if a container was successful or not.

    .. code:: python

      >>> from returns.maybe import Some, Nothing
      >>> from returns.result import Failure, Success
      >>> from returns.io import IOSuccess, IOFailure

      >>> assert is_successful(Some(1))
      >>> assert not is_successful(Nothing)

      >>> assert is_successful(Success(1))
      >>> assert not is_successful(Failure(1))

      >>> assert is_successful(IOSuccess(1))
      >>> assert not is_successful(IOFailure(1))

    This function can work with containers
    that are instance of :class:`returns.interfaces.unwrappable.Unwrappable`.

    For containers that expose a ``success`` property, this function
    will use it for a side-effect free check.
    For containers that don't, it falls back to trying ``unwrap()``
    and catching ``UnwrapFailedError``.

    """
    success_attr = getattr(type(container), 'success', None)
    if success_attr is not None and isinstance(success_attr, property):
        return container.success  # type: ignore[attr-defined]
    try:
        container.unwrap()
    except UnwrapFailedError:
        return False
    return True
