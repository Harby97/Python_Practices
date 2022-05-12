# [1, 1, 2, 2, 4] -> [1, 2, 4]

from random import random


def remove_duplicates(user_list):
    without_duplicates = []

    for element in user_list:
        if element not in without_duplicates:
            without_duplicates.append(element)

    return without_duplicates

def remove_duplicates_sets(user_list):
    return list(set(user_list))

if __name__ == "__main__":
    random_list = [1, 2, 2, 2, 3, "Platzi", "Platzi", True, 4.6, False]
    print(remove_duplicates_sets(random_list))
    