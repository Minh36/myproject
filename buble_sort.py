n = int(input("Nhập số phần tử của list: "))
lst = list(map(int, input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()))

# Bubble Sort tăng dần
for i in range(n - 1):
    for j in range(n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("List sau khi sắp xếp tăng dần:", lst)



n = int(input("Nhập số phần tử của list: "))
lst = list(map(int, input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()))

# Bubble Sort giảm dần
for i in range(n - 1):
    for j in range(n - i - 1):
        if lst[j] < lst[j + 1]:   # chỉ đổi dấu so sánh
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("List sau khi sắp xếp giảm dần:", lst)