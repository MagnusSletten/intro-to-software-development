from geo_calculator.calculations import find_average 


def test_length_of_string() -> None:
    test_string = "python"  # Arrange: set up the inputs
    length = len(test_string)  # Act: run the thing under test
    assert length == 6  # Assert: check the result

def test_find_average_equal_list():
    number_list = [5,5,5] #arance
    value = find_average(number_list) #act

    assert value == 5 #assert 

def test_find_average_odd_numbers():
    number_list = [2,3]
    value =  find_average(number_list)
    assert value == 2.5