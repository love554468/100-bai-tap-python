# Viết một chương trình để tạo ra và in tuple chứa các số chẵn được lấy từ tuple (1,2,3,4,5,6,7,8,9,10).

# Gợi ý:

# Sử dụng "for" để lặp lại tuple.
# Sử dụng tuple() để tạo ra một tuple từ một danh sách.


a = (1,2,3,4,5,6,7,8,9,10)
def sol():
    l = []
    for i in a:
        if not i%2:
            l.append(i)
    return (l)

print(sol())