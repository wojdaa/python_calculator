import pytest
from calculator import calculate, parse_expression


@pytest.mark.parametrize(
    "a, b, operation, expected",
    [
        (2, 3, "+", 5),
        (5, 2, "-", 3),
        (4, 3, "*", 12),
        (10, 2, "/", 5),
        (-2.5, 4, "*", -10.0),
        (2.5, 4.5, "+", 7.0),
        (5.5, 2.0, "-", 3.5),
    ],
)
def test_calculate(a, b, operation, expected):
    assert calculate(a, b, operation) == expected

def test_calculate_float_division_approx():
    assert calculate(1, 3, "/") == pytest.approx(1 / 3)

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(10, 0, "/")

def test_invalid_operation():
    with pytest.raises(ValueError):
        calculate(5, 5, "x")

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("  2.5   *   4.0   ", (2.5, 4.0, "*")),
        ("-3.5 + 2.0", (-3.5, 2.0, "+")),
        (" 10 / 2 ", (10.0, 2.0, "/")),
        ("-1.5 - -2.5", (-1.5, -2.5, "-")),
    ]
)
def test_parse_expression(expression, expected):
    assert parse_expression(expression) == expected

@pytest.mark.parametrize(
    "expression",
    [
        "2++3",
        "2+",
        "+2",
        "",
        "   ",
        "(2+3)",
        "2,5 + 4,0",
    ]
)
def test_parse_expression_invalid(expression):
    with pytest.raises(ValueError):
        parse_expression(expression)
