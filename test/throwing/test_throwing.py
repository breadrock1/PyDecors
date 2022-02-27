from src.throwing.throwing import Throwing


@Throwing.catch_exception(throwable=TypeError)
def test_run_safe_method() -> bool:
    return True


@Throwing.catch_exception(throwable=TypeError)
def test_run_safe_method_with_args(arg1: str, arg2: int, arg3: bool) -> str:
    return f'There are following args: "{arg1}", "{arg2}", "{arg3}"'


@Throwing.catch_exception(throwable=TypeError, message="Testing error")
def test_run_unsafe_method_with_message() -> bool:
    raise TypeError('Here is type error!')


@Throwing.catch_exception(throwable=TypeError, traceback=True)
def test_run_unsafe_method_with_traceback() -> bool:
    raise TypeError('Here is type error!')


@Throwing.catch_exception(throwable=TypeError, another_statement='Here is another string!')
def test_run_unsafe_method_with_another_statement() -> str:
    raise TypeError('Here is type error!')


def return_string_value() -> str:
    return 'Here is another result!'


@Throwing.catch_exception(throwable=TypeError, another_action=return_string_value)
def test_run_unsafe_method_with_another_action() -> bool:
    raise TypeError('Here is type error!')


def test_throwing():
    test_run_unsafe_method_with_message()
    test_run_unsafe_method_with_traceback()

    assert test_run_safe_method()
    assert test_run_unsafe_method_with_another_action() == 'Here is another result!'
    assert test_run_unsafe_method_with_another_statement() == 'Here is another string!'
    assert test_run_safe_method_with_args('Denis', 24, True) == 'There are following args: "Denis", "24", "True"'
