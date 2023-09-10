import pytest


@pytest.mark.flaky(reruns=0)  # this wil rerun the failed test case 3 times
@pytest.mark.usefixtures("appium_driver")
class BaseTest:
    """
    This is the base test which will be inherited by all the test class to use fixtues.
    """
    pass
