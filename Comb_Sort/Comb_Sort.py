"""
This program implements Comb Sort algorithm for list that has to be read from file.
Separartor which is used is ","
"""
import random
def Comb_sort(list:list) -> list:
    """
    this function represents Comb Sort algorithm
    """
    # predefining necessary variables
    gap = len(list)
    sorted = False
    #starting algorithm
    while gap > 1 or not sorted:
        # defining initial gap
        gap = max(1, int(gap/1.3))
        # if there is no changes our list is sorted
        sorted = True
        # main iterator
        for i in range(len(list)-gap):
            # index of variable to compare with
            j = i + gap
            # comparing two variables
            if list[i] > list[j]:
                # if first is bigger than second switch them
                list[i], list[j] = list[j], list[i]
                # if there was a switch list is not sorted
                sorted = False
    return list

if __name__ == "__main__":
    list_to_sort = list([random.uniform(0, 1)*1000 for i in range(10)])
    with open("numbers.txt") as file:
        lines = file.readlines()
        list_to_sort = lines[0].split(",")
    list_to_sort = [float(number) for number in list_to_sort]
    print(list_to_sort)
    print(Comb_sort(list_to_sort))
