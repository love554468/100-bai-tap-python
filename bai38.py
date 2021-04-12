# Định nghĩa một hàm có thể tạo ra list chứa các giá trị bình 
# phương của các số từ 1 đến 20 (bao gồm cả 1 và 20), rồi in 5 mục cuối cùng trong list.

# Gợi ý:

# Tương tự bài 37.

def sol(n):
    listt = [i*i for i in range(1,n+1)]
    # print(listt)
    print(listt[-5::])

sol(int(input()))