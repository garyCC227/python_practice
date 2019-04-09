
class Sorting(object):
    def partition(self, arr,low,high):
        i = ( low-1 )         # index of smaller element
        pivot = arr[high]     # pivot

        for j in range(low , high):

            # If current element is smaller than or
            # equal to pivot
            if   arr[j] <= pivot:

                # increment index of smaller element
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]

        arr[i+1],arr[high] = arr[high],arr[i+1]
        return ( i+1 )

    # Function to do Quick sort
    def quickSort(self, arr,low,high):
        if low < high:

            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr,low,high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)

    def insertion_sort(self, list):
        for i in range(1, len(list)):
            #remeber the current value, need to swap it later
            key = list[i]
            #get its prev values
            j = i-1
            while (j>=0 and key < list[j]):
                list[j+1] = list[j]
                j-=1
            list[j+1] = key

    def selection_sort(self, list):
        for i in range(len(list)):

            # Find the minimum element in remaining
            min_idx = i
            for j in range(i+1, len(list)):
                if list[min_idx] > list[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            list[i], list[min_idx] = list[min_idx], list[i]

        return list

    def mergesort(self,list):
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

    '''
    bubble sort: O(n^2)
    '''
    def bubble_sort(self, list):
        l = len(list)
        for i in range(l - 1):
            for j in range(0, l-1-i):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]

if __name__ == '__main__':
    sort = Sorting()
    list = [5, 1, 6, -3, 9, 8]
    sort.quickSort(list, 0, len(list)-1)
    print(list)
