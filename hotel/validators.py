from rest_framework.exceptions import ValidationError as RfValidationError
from django.core.exceptions import ValidationError as DValidationError


def is_digit(v: str, *, message: str = 'Value has to contain only digits', rest: bool = False) -> None:
    if not v.isdigit():
        if rest:
            raise RfValidationError(message)
        else:
            raise DValidationError(message)


def specific_length(v: str, *, length: int, message: str = 'Value has to contain only digits, got {got}', rest: bool = False) -> None:
    if len(v) != length:
        f_msg = message.format(got=len(v))
        if rest:
            raise RfValidationError(f_msg)
        else:
            raise DValidationError(f_msg)
