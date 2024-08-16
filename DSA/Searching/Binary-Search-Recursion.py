def binarySearchRecurssion(arr,low,high,target):
    if low > high:
        return-1
    mid = (low+high)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearchRecurssion(arr,low,mid-1,target)
    else:
        return binarySearchRecurssion(arr,mid+1,high,target)    


arr= [1,2,3,4,5,6,7,8,9,0]
print(binarySearchRecurssion(arr,0,len(arr)-1,3))        
