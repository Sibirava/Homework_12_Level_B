import random
NUMBER = 5
RANDOM_VALUE_UP = 10
RANDOM_VALUE_DOWN = -10
def random_vector_elements():
    n = NUMBER
    vector = [random.randint(RANDOM_VALUE_DOWN, RANDOM_VALUE_UP) for i in range(n)]
    return vector

def enter_vector_elements():
    vector = []

    element = 0

    while element != -1:
        element = int(input("Input element in a row:"))
        if element == -1:
            break
        else:
            vector.append(element)
    return vector