from geo_calculator.calculations import find_average, gardners_equation
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