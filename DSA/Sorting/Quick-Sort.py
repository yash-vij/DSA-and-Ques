arr = [9,8,7,6,5,4,3,2,1]


def quick_sort(arr, low, high):

    if low < high :

        partition_index = partition_func(arr,low,high)
        print("part_index",partition_index)
        quick_sort(arr,low, partition_index-1)
        quick_sort(arr,partition_index+1, high)

def partition_func(arr, low, high):
    pivot = arr[low]
    print("pivot is ",pivot)
    i,j = low,high
    print("i : ",i," and j : ",j)

    while i < j:
        
        while arr[i] < pivot and i < high :
            print("For i : ",arr[i]," <= ",pivot," and ",i," < ",high)
            i = i+1
        while arr[j] > pivot and j > low :
            print("For j : ",arr[j]," >= ",pivot," and ",j," < ",low)
            j = j-1
        print("Final i : ",i," Final j : ",j)
        if i < j :
            temp = arr[i]
            arr[i] = arr[j]         
            arr[j] = temp

    return i

quick_sort(arr,0,len(arr)-1)    
print(arr)