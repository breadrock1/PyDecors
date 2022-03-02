from src.accessible.accessible import Accessible


class TestAccessibleClass(object):

    @staticmethod
    @Accessible.accessible_methods(accessible_methods=['test_run_from_accessible_method'])
    def test_called_function() -> bool:
        return True

    @staticmethod
    def test_run_from_accessible_method() -> bool:
        return TestAccessibleClass.test_called_function()


def test_throwing():
    test_accessible_class = TestAccessibleClass()

    assert test_accessible_class.test_run_from_accessible_method()
