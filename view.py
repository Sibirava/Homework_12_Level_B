import Vector
import Task01
import Task02
import Task03
import Task04
import Task05
import Task06

def main():
    vector = Vector.random_vector_elements()
    module = Task06.find_module_number(vector)

    number = int(input("Input above what number you wanna search: "))
    module_number = Task06.define_module_number(number)

    msg = (f"In vector {vector}: \n"
           f"1)There are {Task01.count_elements_above_number(vector, number)} \n and "
           f"{Task02.count_elements_below_number(vector, number)} \n"
           f"2)There are {Task03.count_elements_equal_number(vector,number)} elements that "
           f"are equal to {number} and {Task04.count_elements_not_equal_number(vector, number)} "
           f"elements that are different from {number} \n"
           f"3)There are {Task05.count_elements_multiple_to_number(vector,number)} elements "
           f"that are multiply to {number} \n"
           f"5)There are {Task06.count_absolute_value_above_number(module, module_number)} elements "
           f"that above module of {number}, "
           f"{Task06.count_absolute_value_below_number(module, module_number)} elements are below "
           f"and {Task06.count_absolute_value_equal_number(module,module_number)} elements are equal")

    print(msg)

main()