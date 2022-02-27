import sys

from logging import error
from typing import Any, AnyStr, Callable, Optional, Type


# TODO: Realize raising exception to user_function
class Throwing(object):

    @staticmethod
    def catch_exception(
            throwable: Type[Exception],
            message: Optional[AnyStr] = None,
            traceback: Optional[bool] = False,
            another_statement: Optional[Any] = None,
            another_action: Optional[Callable] = None,
            # raise_exception: Optional[Type[Exception]] = None
    ) -> Any:

        def wrapper(user_function):

            def wrapped_function(*args):

                try:
                    return user_function(*args)

                except throwable as e:
                    if message:
                        error(msg=message, )

                    if traceback:
                        _trace_back = sys.exc_info()
                        e.with_traceback(_trace_back[2])

                    if another_action:
                        return another_action()

                    if another_statement:
                        return another_statement

                    # if raise_exception:
                    #     raise raise_exception from e

            return wrapped_function

        return wrapper
