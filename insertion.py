# INSERTION SORTING
# DATA : 81,13,29,57,86,56,44,83,78,53
# code reference: programiz

def insertion(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        #comparing key with other elements on the 
        #left until the algorithm finds a smaller element
        while j >= 0 and key < array[j]: 
            array[j + 1] = array[j]
            j = j - 1

        array[j +1] = key

data = [81,13,29,57,86,56,44,83,78,53]
insertion(data)
print('-----------------------------------------------')
print()
print("--> Given data: [81,13,29,57,86,56,44,83,78,53]")
print()
print("-----------------------------------------------")
print()
print(f"---> Sorted data through bubble algorithm:\n{data}")
print()
print("-----------------------------------------------")