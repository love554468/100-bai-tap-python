# Yêu cầu:

# Viết một chương trình Python nhận chuỗi nhập vào bởi người dùng, in "Yes" nếu chuỗi là "yes" hoặc "YES" hoặc "Yes", nếu không in "No".

# Gợi ý:

# Sử dụng lệnh if để kiểm tra điều kiện.

def sol(s):
    return "YES" if s == "Yes" else "NO"

print(sol(input()))