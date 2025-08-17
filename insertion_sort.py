n = int(input("Nhập số phần tử của list: "))
lst = list(map(int, input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()))

# Insertion Sort tăng dần
for i in range(1, n):
    key = lst[i]
    j = i - 1
    while j >= 0 and key < lst[j]:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key

print("List sau khi sắp xếp tăng dần:", lst)





n = int(input("Nhập số phần tử của list: "))
lst = list(map(int, input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()))

# Insertion Sort giảm dần
for i in range(1, n):
    key = lst[i]
    j = i - 1
    while j >= 0 and key > lst[j]:   # đảo dấu so sánh
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key

print("List sau khi sắp xếp giảm dần:", lst)

