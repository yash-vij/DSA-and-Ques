arr = [4,5,6,2,4,45,6,78768,324324,324,23,32,546,6,6,34,5,45,45,67,567]

for i in range(0,len(arr)):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        temp = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = temp
        j = j-1

print(arr)    



