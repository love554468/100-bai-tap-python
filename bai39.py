# Câu hỏi:

# Định nghĩa một hàm có thể tạo list chứa giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20). 
# Sau đó in tất cả các giá trị của list, trừ 5 mục đầu tiên.

# Gợi ý:

# Tương tư bài 37, 38.

def sol(n):
    listt = [ i*i for i in range(1,n+1)]
    print(listt)
    print(listt[5:])

sol(int(input()))