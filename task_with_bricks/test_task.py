import pytest
from .task import makeBricks


@pytest.fixture(scope='function',
                params=[(3, 1, 8, True),
                        (3, 1, 9, False),
                        (2, 3, 9, False)])
def param_test(request):
    return request.param


def test_answer(param_test):
    (a, b, n, expected_output) = param_test
    result = makeBricks(a, b, n)
    assert result == expected_output
