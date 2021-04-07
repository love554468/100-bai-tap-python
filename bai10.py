# Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

# Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

# # Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

nhapXY = input("Nhap X, Y: ")
col = nhapXY.split(",")[1]
row = nhapXY.split(",")[0]
# print(col)
# print(num)
# multilist = [[0 for cot in range(col) ] for hang in range(row)]
multilist = [[0 for col in range(int(col))] for row in range(int(row))]
# print(multilist)
for x in range(int(row)):
    for y in range(int(col)):
        multilist[x][y] = x*y

print(multilist)

