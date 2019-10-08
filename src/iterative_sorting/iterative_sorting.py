arr = [1, 3, 5, 7, 10, 6, 2, 0, 4, 8]

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # print(f"current index {cur_index}")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # print(arr[cur_index])
        for j in range(cur_index, len(arr)):
            # print(arr)
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

arr = [1, 3, 5, 7, 10, 6, 2, 0, 4, 8] #reset my array

    # Keywords that imply a loop is required
    #     while / for
    #     as long as
    #     until
    # Conditions that can be checked with if/else blocks
    #     when we find __
    #     if __ happens
    #     once this value is large/smaller
    # What type of value should be returned?


# def bubble_sort(elements):  # If `elements` is a collection, remember it will be passed by reference, not value

  # We only need to loop through `elements` until we make a pass that leads to 0 swaps. How do we keep track of whether or not any swaps have occurred? #create a swap variable to keep track
  # Do we always need to loop through all elements?
    # Depending on how our loop was set up, which neighbors should be compared?
    # Can we do swaps in Python without a `temp` variable?
    # only the guys on the right hand side matter for what we're looking at in a bubble sort

  # What, if anything needs to be returned?
  # the array


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(arr) - 1):
            # print(f"index: {i}, array item in that index: {arr[i]}")
            #if the current number is bigger than the number directly to the right [i+1], we need to swap them
            if arr[i] > arr[i + 1]:
                print(arr[i])
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap = True
                # brady wrote items[i], items[i+1] = items[i+1], items[i] called it an "inline swap" this can be refactored similarly in selection sort too and I think that makes sense and is simpler.
    return arr


    """ recursion sort
    
    """

print(bubble_sort(arr))



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr