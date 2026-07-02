from geo_calculator.calculations import find_average, gardners_equation,inverse_gardners_equation
import pytest 

def test_length_of_string() -> None:
    test_string = "python"  # Arrange: set up the inputs
    length = len(test_string)  # Act: run the thing under test
    assert length == 6  # Assert: check the result

def test_find_average_equal_list():
    number_list = [5,5,5] #arance
    value = find_average(number_list) #act

    assert value == 5 #assert 

def test_find_average_odd_numbers():
    number_list = [2,3] #Arrange
    value =  find_average(number_list)
    assert value == 2.5

def test_gardners_equation() -> None:
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)

def test_inverse_gardners_equation() -> None:
    density = 2.0730949  # g/cm3
    expected_velocity = 2000  # m/s

    assert inverse_gardners_equation(density) == pytest.approx(expected_velocity)

    assert inverse_gardners_equation(
        gardners_equation(expected_velocity)
    ) == pytest.approx(expected_velocity)

    assert gardners_equation(inverse_gardners_equation(density)) == pytest.approx(
        density
    )
    
@pytest.mark.parametrize(
    "velocity, expected_density",
    [
        (2000, 2.0730949),
        (3000, 2.2942567),
        (4000, 2.4653393),
    ],
)
def test_gardners_equation_multiple_values(
    velocity: float, expected_density: float
) -> None:
    assert gardners_equation(velocity) == pytest.approx(expected_density)

def test_gardners_equation_negative_velocity() -> None:
    velocity = -1000  # m/s
    with pytest.raises(ValueError) as e:
        gardners_equation(velocity)


def test_inverse_gardners_equation_negative_density() -> None:
    density = -1000  # g/cm3
    with pytest.raises(ValueError) as e:
        inverse_gardners_equation(density)