# SELECTION SORTING
# DATA : 81,13,29,57,86,56,44,83,78,53
# code reference: programiz

def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quick(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quick(array, low, pi - 1)

        quick(array, pi + 1, high)

data = [81,13,29,57,86,56,44,83,78,53]
print('-----------------------------------------------')
print()
print("--> Given data: [81,13,29,57,86,56,44,83,78,53]")
print()
size = len(data)
quick(data, 0, size -1)
print("-----------------------------------------------")
print()
print(f"---> Sorted data through quick sorting algorithm:\n{data}")
print()
print("-----------------------------------------------")