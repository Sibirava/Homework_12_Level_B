def count_elements_multiple_to_number(vector, number):
    count = 0
    for element in vector:
        if element % number == 0:
            count += 1
    return count