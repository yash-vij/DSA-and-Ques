def mergeSort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]


        #recursion
        mergeSort(left_arr)
        mergeSort(right_arr)

        i = 0
        j = 0
        k = 0

        #merge
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1   

        while i < len(left_arr):
            arr[k] = left_arr[i] 
            i += 1
            k += 1       

        while j < len(right_arr):
            arr[k] = right_arr[j] 
            j += 1
            k += 1

arr = [9,8,7,6,5,4,3,2,1]
mergeSort(arr)
print(arr)