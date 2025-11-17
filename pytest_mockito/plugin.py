
import pytest
from _pytest.outcomes import Failed


_PLUGIN_FIXTURES = {"unstub", "when", "when2", "expect", "patch", "spy2"}


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    from mockito import (
        unstub, verifyStubbedInvocationsAreUsed, verifyNoUnwantedInteractions
    )

    # Let pytest (and other plugins) run the actual test call.
    outcome = yield

    fixturenames = getattr(item, "fixturenames", ())
    used_fixtures = _PLUGIN_FIXTURES.intersection(fixturenames)

    exc = None
    if used_fixtures:
        try:
            verifyStubbedInvocationsAreUsed()
            if "expect" in fixturenames:
                verifyNoUnwantedInteractions()
        except Exception as e:
            exc = e
        finally:
            unstub()

    if exc is not None:
        # Turn the mockito verification error into a clean pytest failure.
        outcome.force_exception(Failed(str(exc), pytrace=False))


@pytest.fixture
def unstub():
    from mockito import unstub
    return unstub


@pytest.fixture
def when(unstub):
    from mockito import when
    return when


@pytest.fixture
def when2(unstub):
    from mockito import when2
    return when2


@pytest.fixture
def expect(unstub):
    from mockito import expect
    return expect


@pytest.fixture
def patch(unstub):
    from mockito import patch
    return patch


@pytest.fixture
def spy2(unstub):
    from mockito import spy2
    return spy2
