import math
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for item in range(0, elements):
        # print(item)
        if len(arrA) > 0:
            if len(arrB) > 0:
                if arrA[0] < arrB[0]:
                    merged_arr[item] = arrA[0]
                    arrA = arrA[1:]
                else:
                    merged_arr[item] = arrB[0]
                    arrB = arrB[1:]
            else:
                    merged_arr[item] = arrA[0]
                    arrA = arrA[1:]
        else:
            merged_arr[item] = arrB[0]
            arrB = arrB[1:]
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    pivot = math.floor(len(arr)/2)
    # print(pivot)
    arrL = []
    arrR = []
    for item in range(0, len(arr)):
        if item < pivot:
            arrL.append(arr[item])
        else:
            arrR.append(arr[item])
    if len(arrL) > 1:
        print(arrL)
        arrL = merge_sort(arrL)
    if len(arrR) > 1:
        arrR = merge_sort(arrR)
    arr = merge(arrL, arrR)
    return arr

print(merge_sort([1,3,2,4,6,5,4,3,2,1]))
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
