''''
stable sorting means 每一次sort之后都是一样的结果。
''''

''''''''''''''''
Merge sort : a divide and conquer algorithm
''''''''''''''''


'''''''''''''''''
 - Time complexity = O(NlogN)
 - stable
 - how it works:
    1) divide the array into two subarray recursively
    2) sort the subarray with mergesort recursively
    3) if only 1 item in subarray, we defind it as sorted
    4) merge the subarray to get the final sorted array

how to divide : 看图！
how to conquer:
    so two subarray A, B ->
    start from A[0] and B[0]， 然后一个一个compare, 小的那个放进result array,
    然后increase index 1 for (小的那边的那个subarray). 然后一直一直compare到
    最后
'''''''''''''''''


'''
selection sort/ insertion sort
'''

'''
    - time complexity : O(n^2)
    - not stable/ stable
    - selection sort: compare to remeber the min of each round, finally swap; each loop is in range i+1, len(list)
    - insertion sort: shift a lot if pre is larger than next. so it will take the curr num to compare all the prev values
'''

'''
quick sort
'''

'''
 - time complexity: average: O(nlogn), but worst case is O(n^2)
 - not stable
 - how it works:
    - divide and conquer algorithm
    - select a pivot, then let all the smaller value stay in its left, larger values stay in its right. and recursively put its left sub-subarray
    and its right sub-right into recursion.

'''
