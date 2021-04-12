# Viết chương trình Python dùng map() để tạo list chứa các giá trị bình phương của các số trong [1,2,3,4,5,6,7,8,9,10].

# Gợi ý:

# Sử dụng map() để tạo list.
# Sử dụng lambda để định nghĩa hàm chưa biết.

def sol():
    return list(map(lambda x:x**2,[1,2,3,4,5,6,7,8,9,10]))

print(sol())