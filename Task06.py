def find_module_number(vector):
    module_list = []
    for element in vector:
        if element < 0:
            module = element * (-1)
        elif element == 0:
            module = 0
        else:
            module = element
        module_list.append(module)
    return module_list

def define_module_number(number):
    module_number = 0

    if number < 0:
        module_number = number * (-1)
    elif number > 0:
        module_number = number
    return module_number

def count_absolute_value_above_number(module, module_number):
    count = 0

    for element in module:
        if element > module_number:
            count += 1
    return count

def count_absolute_value_below_number(module, module_number):

    count = 0

    for element in module:
        if element < module_number:
            count += 1
    return count

def count_absolute_value_equal_number(module, module_number):

    count = 0

    for element in module:
        if element == module_number:
            count += 1
    return count