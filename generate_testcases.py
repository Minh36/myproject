def main():
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    lst = []
    print("Nhập các phần tử:")
    for i in range(n):
        num = int(input(f"Phần tử thứ {i+1}: "))
        lst.append(num)

    asc_lst = sorted(lst)
    desc_lst = sorted(lst, reverse=True)

    print("\n Danh sách ban đầu:", lst)
    print(" Danh sách tăng dần:", asc_lst)
    print(" Danh sách giảm dần:", desc_lst)

    with open("C:/Users/caomi/Documents/PythonOutput/testcase.txt", "w", encoding="utf-8") as f:
        f.write(" Danh sách ban đầu: " + str(lst) + "\n")
        f.write(" Danh sách tăng dần: " + str(asc_lst) + "\n")
        f.write(" Danh sách giảm dần: " + str(desc_lst) + "\n")

    print("\n Kết quả đã được lưu vào file 'testcase.txt'.")
if __name__ == "__main__":
    main()