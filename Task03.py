
def count_elements_equal_number(vector, number):
    count = 0
    for element in vector:
        if element == number:
            count += 1
    return (count)