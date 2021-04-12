# Yêu cầu:

# Dãy Fibonacci được tính dựa trên công thức sau:

# f(n)=0 nếu n=0

# f(n)=1 nếu n=1

# f(n)=f(n-1)+f(n-2) nếu n>1

# Hãy viết chương trình sử dụng list comprehension để in dãy Fibonacci dưới dạng tách biệt bằng dấu ",", n được người dùng nhập vào.

# Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của chương trình sẽ là: 0,1,1,2,3,5,8,13

# Gợi ý:

def f(n):
    return n if n<2 else f(n-1) + f(n-2)

def sol(n):
    lst = [str(f(i)) for i in range(2,n+1)]
    return ",".join(lst)


print(sol(int(input())))