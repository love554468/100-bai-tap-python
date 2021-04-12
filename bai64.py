# Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với một n là số được nhập vào (n> 0).

# Ví dụ, nếu n là số sau đây được nhập vào:

# 5

# Thì đầu ra phải là:

# 3.55

def sol(n):
    s = 0 
    for i in range(1,n+1):
        s += i/(i+1)
    return round(s,2)

print(sol(int(input())))