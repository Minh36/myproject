
# Bubble Sort
def bubble_sort(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, count


# Insertion Sort
def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1
        count += 1  # tính lần kiểm tra cuối cùng khi vòng while dừng
        arr[j + 1] = key
    return arr, count


# Selection Sort
def selection_sort(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            count += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, count



# Merge Sort
def merge_sort(arr):
    def merge(left, right):
        result = []
        i = j = count = 0
        while i < len(left) and j < len(right):
            count += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result, count

    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, count_left = merge_sort(arr[:mid])
    right, count_right = merge_sort(arr[mid:])
    merged, count_merge = merge(left, right)
    return merged, count_left + count_right + count_merge


    return arr
