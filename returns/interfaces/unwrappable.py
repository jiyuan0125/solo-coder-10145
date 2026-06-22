from abc import abstractmethod
from typing import Generic, TypeVar

from returns.primitives.exceptions import UnwrapFailedError

_FirstType = TypeVar('_FirstType')
_SecondType = TypeVar('_SecondType')

_UnwrappableType = TypeVar('_UnwrappableType', bound='Unwrappable')


class Unwrappable(Generic[_FirstType, _SecondType]):
    """
    Represents containers that can unwrap and return its wrapped value.

    There are no aliases or ``UnwrappableN`` for ``Unwrappable`` interface.
    Because it always uses two and just two types.

    Not all types can be ``Unwrappable`` because we do require
    to raise ``UnwrapFailedError`` if unwrap is not possible.
    """

    __slots__ = ()

    @abstractmethod
    def unwrap(self: _UnwrappableType) -> _FirstType:
        """
        Custom magic method to unwrap inner value from container.

        Should be redefined for ones that actually have values.
        And for ones that raise an exception for no values.

        .. note::
            As a part of the contract, failed ``unwrap`` calls
            must raise :class:`returns.primitives.exceptions.UnwrapFailedError`
            exception.

        This method is the opposite of :meth:`~Unwrapable.failure`.
        """

    @abstractmethod
    def failure(self: _UnwrappableType) -> _SecondType:
        """
        Custom magic method to unwrap inner value from the failed container.

        .. note::
            As a part of the contract, failed ``failure`` calls
            must raise :class:`returns.primitives.exceptions.UnwrapFailedError`
            exception.

        This method is the opposite of :meth:`~Unwrapable.unwrap`.
        """

    @property
    def is_success(self) -> bool:
        """
        Side-effect-free check whether the container represents success.

        Default implementation uses ``unwrap`` which may have side effects.
        Concrete containers should override this with a constant value.

        .. code:: python

          >>> from returns.result import Success, Failure
          >>> assert Success(1).is_success is True
          >>> assert Failure(1).is_success is False

        """
        try:
            self.unwrap()
        except UnwrapFailedError:
            return False
        return True
