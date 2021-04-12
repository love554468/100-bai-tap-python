# Viết một chương trình để tạo tuple khác, chứa các giá trị là số chẵn trong tuple (1,2,3,4,5,6,7,8,9,10) cho trước.

# Gợi ý:

# Sử dụng for để lặp tuple.
# Sử dụng tuple() để tạo tuple từ list.
# Code mẫu:


a = (1,2,3,4,5,6,7,8,9,10)
l = len(a)
def sol():
    tup_new = ([i%2 == 0 for i in range(1,l+1)])
    print(tup_new)

sol()