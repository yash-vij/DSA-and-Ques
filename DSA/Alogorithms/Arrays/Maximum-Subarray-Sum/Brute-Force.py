def maxSubSum(arr):
    maxSum = min(arr)
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
            maxSum = max(sum,maxSum)



    return maxSum 



arr = [-1,-2,-3,3,4,6]

print(maxSubSum(arr))

        

