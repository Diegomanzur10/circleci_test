from code.main import Add
import pytest

@pytest.mark.parametrize(
    ("a",
     "b",
     "expected_val"),
    [
        (
            3,
            4,
            7,
        ),
        (
            -1.0,
            -2.0,
            -3.0
        )
    ],
    ids=[
        "test1",
        "test2",
    ]
)
def test_add(a: float, b: float, expected_val:float) -> None:
    assert Add(a, b) == expected_val