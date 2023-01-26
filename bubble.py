# BUBBLE SORTING
# DATA : 81,13,29,57,86,56,44,83,78,53
# code reference: programiz

def bubble(array):
    for i in range(len(array)): #access elements

        for j in range(0, len(array) - i - 1): #compare elements

            if array[j] > array [j + 1]: #comparing adjacent elements
                
                #elements swapping
                temp = array[j]  
                array[j] = array[j + 1]
                array[j+1] = temp





