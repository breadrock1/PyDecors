import inspect
from typing import Any, List

from src.accessible.NonAccessibleMethodException import NonAccessibleMethodException


class Accessible(object):

    @staticmethod
    def accessible_methods(accessible_methods: List[str]) -> Any:

        def wrapper(user_function):

            def wrapped_function(*args):
                current_frame = inspect.currentframe()
                outer_frames = inspect.getouterframes(current_frame, 2)
                caller_function_name = outer_frames[1][3]

                if caller_function_name not in accessible_methods:
                    raise NonAccessibleMethodException('The calling function has been blocked!')

                return user_function(*args)

            return wrapped_function

        return wrapper
