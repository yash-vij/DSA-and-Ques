arr = [14,435,564,657,324,58,970,43532,32,34,456,567,57,8,76]

#We select the minimum and replace with first element and so on
# Worst and Average case time comp. is O(n2)


for i in range(0,len(arr)-1):       # loop till n-2 because comparision will be done till second last
    mini = i
    for j in range(i,len(arr)):
        if arr[mini] > arr[j]:
            mini = j
    temp = arr[i]
    arr[i] = arr[mini]
    arr[mini]= temp


print(arr)            

