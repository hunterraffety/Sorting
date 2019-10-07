arr = [1, 3, 5, 7, 10, 6, 2, 0, 4, 8]

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # print(arr[cur_index])
        for j in range(cur_index, len(arr)):
            print(f"this is arr {arr}, this is j: {arr[j]}, this is the current index: {cur_index}")


        # TO-DO: swap




    return arr

selection_sort(arr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr