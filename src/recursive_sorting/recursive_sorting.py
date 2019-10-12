# TO-DO: complete the helper function below to merge 2 sorted arrays
'''
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
            #print(arrB[j], merged_arr[i])
            merged_arr[i] = arrB[j]
            j += 1 # ends
        elif i >= len(arrB):  # this guy is empty
            #print(arrA[i], merged_arr[i])
            merged_arr[i] = arrA[i]
            i =+ 1 # ends
    # while i < len(arrA) and j < len(arrB):
        # current = i
        elif arrA[i] < arrB[j]: # element at this location is smaller
            #print(arrA[i], merged_arr[i])
            merged_arr[i] = arrA[i]
            # merged_arr.append(arrA[i]) #appends item, but at the end, doesn't overwrite the zeros that were populated based on the elements
            i += 1 # increment the index item
        else: # element at arrB is smaller
            #print(arrB[j], merged_arr[i])
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
# def merge_sort( arr ):
    # TO-DO
    # need to check the array is large enough
    # need to split arr into two. // by 2
    # need to define which sides are which by recursively calling merge_sort
    # need to join with merge helper function
    # return arr


arr = [1, 3, 5, 7, 2, 4, 6, 8]
'''
# solution from lecture 10.09.19

def merge(arrA, arrB):
    #merge step takes two sorted arrays, merge them to a single sorted array containing all elements from both arrays
    #create a new array, length of lenArrA, lenArrB
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements # avoids shifting and copying, efficiency
    #create markers for a and b starting at 0
    a = 0
    b = 0
    #while a and b are less than the length of arrA and arrB respectively
    #compare the items at indices a/b, add smallest to merged array
    #increment a or b, depending on which was smallest
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else: # arrA[a] >= arrB[b]:
            merged_arr[i] = arrB[b]
            b += 1
    print(f"MERGED: {merged_arr}")
    return merged_arr



arr = [1, 3, 5, 7, 2, 4, 6, 8, 3]
def merge_sort(arr):
    print(f"merge sort: {arr}")
    #take in unsorted lists
    #return a sorted list
    if len(arr) <= 1: # Base Case
        return arr  # Base Case
    else:
        #split this in half, sort the halves
        left_half =  arr[0 : len(arr) // 2] #splices first half off #something
        right_half =  arr[len(arr) // 2 : ] #this one splices last half off #something
        #merge the sorted halves
        left_sorted = merge_sort(left_half)
        right_sorted = merge_sort(right_half)
        return merge(left_sorted, right_sorted)

merge_sort(arr)



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