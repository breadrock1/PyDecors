import asyncio
from functools import wraps
from typing import Any, Callable

from src.asyncrun.async_execution_exception import (
    AsyncRuntimeException,
    AsyncValueErrorException
)


class Asyncrun(object):

    @staticmethod
    async def async_user_function(function: Callable, *args) -> Any:
        return function(*args)

    @staticmethod
    def async_run(user_function) -> Any:

        @wraps(user_function)
        def wrapped_function(*args):
            try:
                result = asyncio.run(Asyncrun.async_user_function(user_function, *args))
                return result

            except RuntimeError as e:
                raise AsyncRuntimeException from e

            except ValueError as e:
                raise AsyncValueErrorException from e

        return wrapped_function
