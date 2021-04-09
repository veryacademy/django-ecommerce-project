import pytest


@pytest.mark.core
def test_hello_world3(test_fixture1):
    print("function_fixture3")
    assert test_fixture1 == 1
