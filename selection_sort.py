n = int(input("Nhập số phần tử của list: "))
lst = list(map(int, input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()))

# Selection Sort tăng dần
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]

print("List sau khi sắp xếp tăng dần:", lst)




n = int(input("Nhập số phần tử của list: "))
lst = list(map(int, input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()))

# Selection Sort giảm dần
for i in range(n):
    max_index = i
    for j in range(i + 1, n):
        if lst[j] > lst[max_index]:   # chọn phần tử lớn nhất
            max_index = j
    lst[i], lst[max_index] = lst[max_index], lst[i]

print("List sau khi sắp xếp giảm dần:", lst)
