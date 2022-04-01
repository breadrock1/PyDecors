import inspect
from typing import Any, List
from functools import wraps

from src.accessible.non_accessible_method_exception import NonAccessibleMethodException


class Accessible(object):

    @staticmethod
    def accessible_methods(accessible_methods: List[str], exclude: List[str]) -> Any:

        def wrapper(user_function):

            @wraps(user_function)
            def wrapped_function(*args):
                current_frame = inspect.currentframe()
                outer_frames = inspect.getouterframes(current_frame, 2)
                caller_function_name = outer_frames[1][3]

                if caller_function_name not in accessible_methods:

                    if caller_function_name not in exclude:
                        raise NonAccessibleMethodException('The calling function has been blocked!')

                    return

                return user_function(*args)

            return wrapped_function

        return wrapper
