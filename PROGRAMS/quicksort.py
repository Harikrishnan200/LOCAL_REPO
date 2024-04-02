def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def partition(array, low, high):
    pivot = array[low]
    start = low + 1
    end = high

    while start <= end:
        while  array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        
        if start < end:
            swap(array, start, end)

    # Swap pivot with end
    swap(array, low, end)
    return end

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
