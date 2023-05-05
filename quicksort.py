'''
choose pivot element (last or random)
elements less than pivot go left
elements greater than pivot go right
quicksort recursively on sides of the pivot
'''

def quickSort(arr, left, right):
    # if 1 element left, return immediately
    # or if pointers are not aligned
    if left < right:
        pivot_index = partition(arr, left, right)
        # recursively call quick on sides of pivot
        quickSort(arr, left, pivot_index -  1)
        quickSort(arr, pivot_index + 1, right) 


# partition helper function
# returns index or pivot element
def partition(arr, left, right):
    print(arr, left, right)

    i, j = left, right - 1
    # pivot is last element in array
    pivot = arr[right]

    # i moves right, j moves left, until they cross positions
    while i < j:
        # i moves right until end of array or an element greater than pivot is found
        while i < right and arr[i] < pivot:
            i += 1
        # j moves left until start of array or an element less than pivot is found
        while j > left and arr[j] >= pivot:
            j -= 1
        
        # when smaller and larger elements are found, if i is smaller than j, swap their positions
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # after loop
    # if a larger element was found, swap with pivot position
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    # return i as new pivot index
    return i


arr = [22, 11, 88, 66, 55, 77, 33, 44]
# array is modified in place
quickSort(arr, 0, len(arr) - 1)
print(arr)