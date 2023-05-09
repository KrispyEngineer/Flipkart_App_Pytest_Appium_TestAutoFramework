import pytest

@pytest.mark.flaky(reruns=4)
@pytest.mark.usefixtures('setup_function', 'log_on_failure')
class BaseTest:
    pass
