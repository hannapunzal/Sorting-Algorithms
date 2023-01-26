# MERGE SORTING
# DATA : 81,13,29,57,86,56,44,83,78,53
# code reference: programiz

def merge(array):
    if len(array) > 1 :
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        merge(L)
        merge(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def print_list(array):
    for i in range(len(array)):
        print(array[i], end="")

    print()

if __name__ == '__main__':
    array = [81,13,29,57,86,56,44,83,78,53]

    merge(array)

    print('-----------------------------------------------')
    print()
    print("--> Given data: [81,13,29,57,86,56,44,83,78,53]")
    print()
    print("-----------------------------------------------")
    print()
    print(f"---> Sorted data through merge algorithm:\n{array}")
    print()
    print("-----------------------------------------------")


