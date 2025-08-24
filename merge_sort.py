def merge_sort_desc(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_desc(left)
        merge_sort_desc(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
n = int(input("Nhập số phần tử của list: "))
lst = list(map(int, input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()))
print("Merge Sort giảm dần:", merge_sort_desc(lst))

# Merge sort giảm dần




def merge_sort_asc(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_asc(left)
        merge_sort_asc(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:   
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


n = int(input("Nhập số phần tử của list: "))
lst = list(map(int, input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()))
print("Merge Sort tăng dần:", merge_sort_asc(lst))

# Merge sort tăng dần




