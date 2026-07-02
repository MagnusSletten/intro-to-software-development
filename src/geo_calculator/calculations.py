def find_average(number_list: list):
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """
    sum = 0

    for number in number_list:
        sum += number
    return sum / len(number_list)


def gardners_equation(velocity):
    """Calculate bulk density
    Args:
        velocity: Velocity in m/s
    Returns:
        bulk density
    """

    if velocity < 0:
        raise (ValueError("Velocity cannot be negative"))

    return 0.31 * velocity**0.25


def inverse_gardners_equation(density):

    velocity = (density / 0.31) ** (1 / 0.25)

    if density < 0:
        raise (ValueError("Density cannot be negative"))

    return velocity
