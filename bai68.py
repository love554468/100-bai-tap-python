# Yêu cầu:

# Viết chương trình sử dụng generator để in số chẵn trong khoảng từ 0 đến n, cách nhau bởi dấu phẩy, n là số được nhập vào.

# Ví dụ nếu n=10 được nhập vào thì đầu ra của chương trình là: 0,2,4,6,8,10

# Gợi ý:

# Sử dụng yield để tạo ra giá trị kết tiếp trong generator.

def en(n):
    for i in range(0,n+1):
        if not i%2:
            yield i


n = int(input())
l = []
for i in en(n):
    l.append(str(i))

print(",".join(l))