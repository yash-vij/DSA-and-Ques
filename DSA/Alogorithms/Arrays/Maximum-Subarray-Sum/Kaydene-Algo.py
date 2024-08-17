import sys

def maxSubArraySum(arr):
    max_sum = -sys.maxsize -1

    sum = 0
    
    for i in range(0,len(arr)):
        sum = sum + arr[i]

        if sum < 0:
            sum = 0

        if sum > max_sum :
            max_sum = sum

    return max_sum

arr = [-2,-3,4,-1,-2,1,5,-3]
print(maxSubArraySum(arr))      