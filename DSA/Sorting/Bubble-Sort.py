arr = [1213,345,435,6,54,654,4567,567,78,76,867,867,8,768,7567,345]

for i in range(len(arr)-1,0,-1):
    for j in range(0,i):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)    

