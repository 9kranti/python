"""
19. Swap multiple elements in the list
"""

from random import randint

def swap_multiple():
    list1 = [1,2,3,4,5,6]
    list2 = []
    temp_index = []
    for i in range(len(list1)):
        while True:
            random_index = randint(0, len(list1) - 1)
            if random_index in temp_index:
                continue
            else:
                if random_index == 0 and len(list2) == 0 and i == 0:
                    pass
                else:
                    list2.append(list1[random_index])
                    temp_index.append(random_index)
                    break
    print(list2)

swap_multiple()