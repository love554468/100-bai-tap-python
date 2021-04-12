# Định nghĩa hàm có thể 
# chấp nhận input là số nguyên và in "Đây là một số chẵn" nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ.
def sol(n):
    if n%2:
        print("day la mot so le")
    else:
        print('day la mot so chan')

sol(int(input()))