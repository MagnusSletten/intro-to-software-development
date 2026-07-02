def find_average(number_list: list):
    sum = 0 

    for number in number_list:
        sum += number 
    return sum/len(number_list)

def gardners_equation(velocity):
    return 0.31*velocity**0.25