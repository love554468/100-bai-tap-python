# Dãy Fibonacci được tính dựa trên công thức sau:

# f(n)=0 nếu n=0

# f(n)=1 nếu n=1

# f(n)=f(n-1)+f(n-2) nếu n>1

# Hãy viết chương trình tính giá trị của f(n) với n là số được người dùng nhập vào. Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của chương trình sẽ là 13.

# Gợi ý:

# Tương tự như bài 65, ta cũng sử dụng hàm đệ quy trong Python.

def solFibo(n):
    return n if n<2 else solFibo(n-1)+solFibo(n-2)

print(solFibo(int(input())))