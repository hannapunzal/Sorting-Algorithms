# SELECTION SORTING
# DATA : 81,13,29,57,86,56,44,83,78,53
# code reference: programiz

def selection(array,size):

    for step in range(size):
        min_idx = step
        
        for i in range(step + 1, size):
            if array[i] < array[min_idx]: # choosing the minimum element in every loop
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step]) #putting the array into the correct structure
