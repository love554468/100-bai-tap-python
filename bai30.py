# Định nghĩa một hàm có input là 2 chuỗi và in chuỗi có độ
#  dài lớn hơn trong giao diện điều khiển. Nếu 2 chuỗi có chiều 
# dài như nhau thì in tất cả các chuỗi theo dòng.

def sol(n,m):
    if len(n) == len(m):
        print(n)
        print(m)
    elif len(n)>len(m):
        print(n)
    else:
        print(m)

n = input()
m = input()
sol(n,m)
    