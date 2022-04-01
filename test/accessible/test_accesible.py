from pytest import raises
from typing import NoReturn

from src.accessible.accessible import Accessible
from src.accessible.NonAccessibleMethodException import NonAccessibleMethodException


class TestAccessibleClass(object):

    @staticmethod
    @Accessible.accessible_methods(
        accessible_methods=['test_run_from_accessible_method'],
        exclude=['pytest_pyfunc_call']
    )
    def test_called_function() -> bool:
        return True

    @staticmethod
    def test_run_from_accessible_method() -> bool:
        return TestAccessibleClass.test_called_function()

    @staticmethod
    def test_run_from_non_accessible_method() -> NoReturn:
        with raises(NonAccessibleMethodException):
            TestAccessibleClass.test_called_function()


def test_throwing():
    test_accessible_class = TestAccessibleClass()

    test_accessible_class.test_run_from_non_accessible_method()
    assert test_accessible_class.test_run_from_accessible_method()
