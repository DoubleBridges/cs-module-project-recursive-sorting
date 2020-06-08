import pdb

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Recursively split the array in half until len(all arrays) == 1
    if len(arr) > 1:
        # define midpoint
        m = len(arr) // 2
        # define left half
        l = arr[:m]
        # define right half
        r = arr[m:]

        # Recurse left half
        l = merge_sort(l)
        # Recurse right half
        r = merge_sort(r)

        # Setup pointers for merge
        i = 0  # Traverses left arr
        j = 0  # Traverses right arr
        k = 0  # Traverses arr for inserting values into sorted location
        # pdb.set_trace()
        # Iterate through l and r simultaneously,
        # find smallest value between current index in l and r
        # and insert it at arr[k], inc k as you go
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        # Cleanup left over elements from uneven arr's
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    return arr


# implement an in-place merge sort algorithm

"""
    Merge in place is accomplished by passing pointers that locate the limits of the subarrays 
    as opposed to creating the subarrays themselves
"""
# Merges the two subarrays
# First subarray is arr[start:mid]
# Second subarray is arr[mid+1:end]
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1
    print(start, mid, end)

    # If in the correct order
    if arr[mid] <= arr[start2]:
        return

    # Simultaneously iterate through the two subarrays
    while start <= mid and start2 <= end:
        # If the the current left most value is the smallest, move on
        if arr[start] <= arr[start2]:
            start += 1
        else:
            # Store start2's value and poistion
            value = arr[start2]
            index = start2

            # Use start2's stored position to shift all values between
            # start and start2 by 1 index, ( inclusive of start )
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            # Assign start2's value in it's sorted position
            arr[start] = value

            # Inc all pointers
            start += 1
            mid += 1
            start2 += 1

    return arr


# l and r are the pointers  for the left and right subarray to be sorted
def merge_sort_in_place(arr, l, r):
    print(l, r)
    if l < r:
        # m is the mid point us to create the two subarrays
        m = l + (r - l) // 2
        # Recurse both subarrays
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        # Perform the actual sorting on the way back out
        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
