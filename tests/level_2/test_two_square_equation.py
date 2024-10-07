import pytest
from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__negative_discriminant():
    square_coefficient = 0.1
    linear_coefficient = -1.5
    const_coefficient = 10

    solution = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert solution == (None, None)


def test__solve_square_equation__no_square_coefficient():
    square_coefficient = 0
    linear_coefficient = 7.3
    const_coefficient = 2.1

    solution = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert solution == (-0.28767123287671237, None)


def test__solve_square_equation__no_square_no_linear_coefficient():
    square_coefficient = 0
    linear_coefficient = 0
    const_coefficient = 5

    solution = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert solution == (None, None)


def test__solve_square_equation__two_different_roots():
    square_coefficient = 0.1
    linear_coefficient = -2
    const_coefficient = 0.999

    solution = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert solution == (0.5126399878575283, 19.48736001214247)


def test__solve_square_equation__one_root():
    square_coefficient = 1
    linear_coefficient = 2
    const_coefficient = 1

    solution = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert solution == (-1.0, -1.0)


def test__solve_square_equation__wrong_coefficients():
    square_coefficient = "1"
    linear_coefficient = "2"
    const_coefficient = "1"

    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
