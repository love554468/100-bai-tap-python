# Định nghĩa một hàm có thể in dictionary chứa key là các số từ 1 đến 3 (bao gồm cả hai số) và các giá trị bình phương của chúng.

# Gợi ý:

# Sử dụng dict[key]=value để nhập mục vào dictionary.
# Sử dụng toán từ ** để lấy bình phương của một số.

def sol(n):
    x = lambda x:x*x
    listt = list(map(x,range(1,n+1)))
    dic = dict()
    for i in range(1,n+1):
        dic[i] = listt[i-1]
    return dic

print(sol(int(input())))
