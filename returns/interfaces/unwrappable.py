from abc import abstractmethod
from typing import Generic, TypeVar

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

    @property
    @abstractmethod
    def is_successful(self: _UnwrappableType) -> bool:
        """
        Returns ``True`` if the container is in a successful state.

        This property is side-effect free and can be used to check
        if ``unwrap()`` will succeed without actually calling it.

        .. code:: python

          >>> from returns.result import Success, Failure
          >>> assert Success(1).is_successful
          >>> assert not Failure(1).is_successful

        """

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
