# Định nghĩa một hàm có thể tạo ra một dictionary 
# chứa key là những số từ 1 đến 20 (bao gồm cả 1 và 20) 
# và các giá trị bình phương của key. Hàm chỉ cần in các key.

def sol(n):
    dic = dict()
    for i in range(1,n+1):
        dic[i] = i**2
    print(dic.keys())

sol(int(input())) 