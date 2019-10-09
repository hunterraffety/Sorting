# TO-DO: complete the helper function below to merge 2 sorted arrays
arrA = [1, 2, 3, 4]
arrB = [5, 6, 7, 8]

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB ) #gives you the total count of elements
    merged_arr = [0] * elements #sets up an empty list for you to append things into?
    # TO-DO
    # print(elements)  # returns count of elements
    # print(merged_arr) # returns 9 empty spaces (given 9 elements)
    # print(arrA[0])
    # starting at beginning of `a` and `b`
    # while arrA and arrB:
    #     for i in range(0, len(arrA) - 1):
    #         for j in range(0, len(arrB) -1):
    #             if arrA[i] < arrB[j]:
    #                 merged_arr.append(arrA[i])
    #             else:
    #                 merged_arr.append(arrB[j])
    # compare the next value of each
    # add smallest to `merged_arr`
    
    # i need to check the value in the first array's index of 0 and determine whether or not it is greater than the second arrays value held in index 0, and depending on that, appending the value to the merged_arr

    # sounds like I need two for loops. The first one needs to keep track of the value of the thing inside of it at the specified index
    i = 0
    j = 0

    for i in range(elements):
        if i >= len(arrA):  # this guy is empty
            print(arrB[j], merged_arr[i])
            merged_arr[i] = arrB[j]
            j += 1 # ends
        elif i >= len(arrB):  # this guy is empty
            print(arrA[i], merged_arr[i])
            merged_arr[i] = arrA[i]
            i =+ 1 # ends
    # while i < len(arrA) and j < len(arrB):
        # current = i
        elif arrA[i] < arrB[j]: # element at this location is smaller
            print(arrA[i], merged_arr[i])
            merged_arr[i] = arrA[i]
            # merged_arr.append(arrA[i]) #appends item, but at the end, doesn't overwrite the zeros that were populated based on the elements
            i += 1 # increment the index item
        else: # element at arrB is smaller
            print(arrB[j], merged_arr[i])
            merged_arr[i] = arrB[j]
            # merged_arr.append(arrB[j])
            j += 1
        # merged_arr = merged_arr + arrA[i:]
        # merged_arr = merged_arr + arrB[j:]
        # print(merged_arr)
    # while len(merged_arr) < elements:
        # for i in range(0, len(arrA) - 1):
        #     for j in range(0, len(arrB) - 1):
        #         print(arrA[i], arrB[j])
        #         if arrA[i] < arrB[j]:
        #             merged_arr.append(arrA[i])
        #         else:
        #             merged_arr.append(arrB[j])

    return merged_arr

print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr








items = [1, 2, 3, 45, 5,12, 1, 3, 4, 5, 6]

def quicksort(items):
    if len(items) <= 1:
        return items
    # select a pivot
    pivot = items[-1]
    left = []
    right = []
    for i in range(0, len(items) -1):
        # move smaller to left
        item = items[i]
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
        # move larger to right
        # lhs / rhs = 1, repeat first 3 steps
    return quicksort(left) + [pivot] + quicksort(right)

# print(quicksort(items))



# def partition(data):
#     left = []
#     pivot = data[0]
#     right = []
#     for v in data[1:]:

def quick_sort_A( books, low, high ):
    # base case
    if low >= high:
        return books
    # recursive case
    else:
        # divide
        pivot_index = low
        # for each element in subarray
        for i in range(low, high):
            if books[i].genre < books[pivot_index].genre:
                # double swap to move smaller elements to correct index
                # move current element to the right of pivot
                temp = books[pivot_index+1]
                books[pivot_index+1] = books[i]
                books[i] = temp
                # swap pivot with element on its right
                temp = books[pivot_index]
                books[pivot_index] = books[pivot_index+1]
                books[pivot_index+1] = temp
                pivot_index += 1
        # conquer
        # Quick Sort everything left of the pivot
        books = quick_sort_A(books, low, pivot_index)
        # Quick Sort everything right of the pivot
        books = quick_sort_A(books, pivot_index+1, high)
        return books