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
