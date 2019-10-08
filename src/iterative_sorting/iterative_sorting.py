arr = [1, 3, 5, 7, 10, 6, 2, 0, 4, 8]

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(f"current index {cur_index}")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # print(arr[cur_index])
        for j in range(cur_index, len(arr)):
            print(arr)
            # print(f"this is arr {arr}, this is j: {arr[j]}, this is the current index: {cur_index}")
            if arr[j] < arr[smallest_index]: # if this current item in this NEW loop is less than what I previously had stored up in that smallest index for the array. Measured against itself. This is why the swap is so important so that I can move them around after each iteration through the array but won't lose track of what is what
                smallest_index = j
                # print(smallest_index, j)
        # TO-DO: swap
        temp = arr[smallest_index] #arr[smallest_index] is the placeholder for when cur_index is being assigned to that value as the new smallest index, so that the current_index can be assigned to the temporary value.
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp



    return arr

print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr