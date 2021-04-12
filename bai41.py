# Với tuple (1,2,3,4,5,6,7,8,9,10) cho trước, viết một chương trình in một nửa số giá 
# trị đầu tiên trong 1 dòng và 1 nửa số giá trị cuối trong 1 dòng.

# Gợi ý:

# Sử dụng [n1:n2] để lấy một phần từ tuple.

# Code mẫu:

a = (1,2,3,4,5,6,7,8,9,10)
l = int(len(a)/2)
def sol():
    print(a[:l])
    print(a[l:])

sol()