def selectionSort(array, size):
    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[i], array[min_index]) = (array[min_index], array[i])


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print(arr)
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)


# section 5

def selection_sort(arr):
    size = len(arr)

    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            # select the minimum element in every iteration
            if arr[j] < arr[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])


num = int(input("Enter the value of num: "))
array = []

print("Enter the elements one by one:")
for _ in range(num):
    element = int(input())
    array.append(element)

selection_sort(array)

print("Sorted array is:")
for element in array:
    print(element)