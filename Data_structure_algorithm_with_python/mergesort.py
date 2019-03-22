'''
merge sort
'''


def mergesort(list):
    #len(1) lsit defined as sorted
    if len(list) == 1:
        return

    #mergesort 1st part: divide
    middle_index = len(list) // 2
    left_list = list[:middle_index]
    right_list = list[middle_index:]

    #recursively divide
    mergesort(left_list)
    mergesort(right_list)


    #mergesort 2nd part: conquer
    i = 0 #index of left subarray
    j = 0 #index of right subarray
    k = 0 #index of result array

    while ( i < len(left_list) and j < len(right_list) ):
        if left_list[i] < right_list[j]:
            list[k] = left_list[i]
            i += 1
        else:
            list[k] = right_list[j]
            j += 1
        k+=1

    #check the remaining elements in left or right subarray
    while( i < len(left_list)):
        list[k] = left_list[i]
        i += 1
        k += 1

    while( j < len(right_list)):
        list[k] = right_list[j]
        j += 1
        k += 1


if __name__ == '__main__':
    list = [5, 1, 6, -3, 9, 8]
    mergesort(list)
    print(list)
