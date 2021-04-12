# Viết chương trình tính: f(n)=f(n-1)+100 khi n>0 và f(0)=1, với n là số được nhập vào (n>0).

# Ví dụ: Nếu n được nhập vào là 5 thì đầu ra phải là 500.

# Gợi ý:

# Chúng ta có thể định nghĩa hàm đệ quy trong Python.

def sol(n):
    return 1 if n ==0 else sol(n-1)+100

print(sol(int(input())))