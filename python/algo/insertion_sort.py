def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

#initialize an empty array
arr = []

# use the for-loop to append elements to the array
for i in range(20):
    x = (3*i+7) % 25
    arr.append(x)

# display the created array
print("The created array is: ", arr)

# Since insertionSort is a function,
# we must pass the array as an argument to it

insertionSort(arr)

# display the sorted array
print("The sorted array is: ", arr)



