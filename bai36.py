# Câu hỏi:

# Định nghĩa một hàm có thể tạo và in list chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20).

# Gợi ý:

# Sử dụng toán tử ** để lấy giá trị bình phương.
# Sử dụng range() cho vòng lặp.
# Sử dụng list.append() để thêm giá trị vào list.
# Code mẫu:

def sol(n):
    liss = []
    for i in range(1,n+1):
        liss.append(i*i)
        print(liss)

sol(int(input()))