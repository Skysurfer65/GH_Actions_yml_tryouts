import pytest

@pytest.fixture
def fixture_func():
   return "fixture test"

def test_fixture(fixture_func):
    assert fixture_func == "fixture test"