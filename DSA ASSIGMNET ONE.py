#NAME -: REDIET ABAY
#ID -:DBU1601572
#1.Write an alternative Python code for simple sorting algorithms,such as insertion and selection sorts.
# Insertion Sort without while loop
arr = [37, 12, 89, 45, 23, 56, 78, 10, 34,92, 15, 74, 38, 51, 67, 29, 83, 46, 58]

for i in range(1, len(arr)):  
    key = arr[i]
    pos = i  

    for j in range(i - 1, -1, -1):  
        if arr[j] > key:
            arr[j + 1] = arr[j]  
            pos = j  
        else:
            break

    arr[pos] = key  

print("Insertion Sort:", arr)       
# Selection Sort using while loop
arr = [37, 12, 89, 45, 23, 56, 78, 10,34,92, 15, 74, 38, 51, 67, 29, 83, 46, 58]
n = len(arr)
for i in range(n - 1):
    min_index = i
    j = i + 1
    while j < n:
        if arr[j] < arr[min_index]:
            min_index = j
        j += 1
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Selection Sort:", arr)

