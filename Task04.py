import Task03
def count_elements_not_equal_number(vector, number):
    result = len(vector) - Task03.count_elements_equal_number(vector, number)
    return result
