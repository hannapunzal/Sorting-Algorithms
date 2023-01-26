# INSERTION SORTING
# DATA : 81,13,29,57,86,56,44,83,78,53
# code reference: programiz

def insertion(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j +1] = key