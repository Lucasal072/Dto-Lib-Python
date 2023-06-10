from typing import Callable, Generic, Optional, TypeVar

T = TypeVar('T')

class DtoField(Generic[T]):
    def __init__(self,
                 default: Optional[T] = None,
                 validation_fn: Optional[Callable[..., bool]] = None,
                 required: Optional[bool] = False,
                 help: Optional[str] = '',) -> None:
        self.value = default
        self.required = required
        self.help = help
        self.validation_fn = validation_fn

    @property
    def is_valid(self):
        if self.required and not self.value:
            return False
        if not self.required and not self.value:
            return True
        if self.validation_fn:
            return self.validation_fn(self.value)
        return True

    def __str__(self) -> str:
        return str(self.value)

    def set_value(self, value: T):
        self.value = value
