# Định nghĩa một hàm có thể tạo list chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20) và in 5 mục đầu tiên trong list.

# Gợi ý:

# Sử dụng toán tử ** để lấy giá trị bình phương.
# Sử dụng range() cho vòng lặp.
# Sử dụng list.append() để thêm giá trị vào list.
# Sử dụng [n1:n2] để cắt list

def sol(n):
    listt = []
    listt = [i*i for i in range(1,n+1)]
    print(listt[:5])

sol(int(input()))