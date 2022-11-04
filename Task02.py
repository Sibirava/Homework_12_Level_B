
def count_elements_below_number(vector, number):
    count = 0
    ls_num = []
    for element in vector:
        if element < number:
            count += 1
            ls_num.append(element)
            msg = f"{count} element(s) BELOW {number} and they are {ls_num}"
    return (msg)