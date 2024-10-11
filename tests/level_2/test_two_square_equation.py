import pytest
from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected_solution",
    [
        (0.1, -1.5, 10, (None, None)),
        (0, 7.3, 2.1, (-0.28767123287671237, None)),
        (0, 0, 5, (None, None)),
        (0.1, -2, 0.999, (0.5126399878575283, 19.48736001214247)),
        (1, 2, 1, (-1.0, -1.0)),
    ],
)
def test__solve_square_equation__different_coefficients(
    square_coefficient, linear_coefficient, const_coefficient, expected_solution
):
    solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected_solution


def test__solve_square_equation__wrong_coefficients():
    square_coefficient = "1"
    linear_coefficient = "2"
    const_coefficient = "1"

    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
