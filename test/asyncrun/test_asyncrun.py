from time import sleep

from pytest import raises
from typing import NoReturn

from src.asyncrun.async_execution_exception import AsyncRuntimeException, AsyncValueErrorException
from src.asyncrun.asyncrun import Asyncrun


class TestAsyncrunClass(object):

    @staticmethod
    @Asyncrun.async_run
    def test_called_function() -> bool:
        sleep(3)
        return True

    @staticmethod
    def run_method_from_another() -> bool:
        return TestAsyncrunClass.test_called_function()

    @staticmethod
    @Asyncrun.async_run
    def run_method_with_runtime_exception() -> NoReturn:
        raise RuntimeError

    @staticmethod
    @Asyncrun.async_run
    def run_method_with_value_error_exception() -> NoReturn:
        raise ValueError


def test_asyncrun():
    test_asyncrun_class = TestAsyncrunClass()

    assert test_asyncrun_class.test_called_function()
    assert test_asyncrun_class.run_method_from_another()

    with raises(AsyncRuntimeException):
        test_asyncrun_class.run_method_with_runtime_exception()

    with raises(AsyncValueErrorException):
        test_asyncrun_class.run_method_with_value_error_exception()
