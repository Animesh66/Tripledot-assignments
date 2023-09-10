import pytest


@pytest.mark.flaky(reruns=0)  # this wil rerun the failed test case 3 times
@pytest.mark.usefixtures("appium_driver")
class BaseTest:
    pass
