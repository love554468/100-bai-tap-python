# Yêu cầu:

# Viết chương trình in list từ list [12,24,35,24,88,120,155,88,120,155], sau khi đã xóa hết các giá trị trùng nhau.

# Gợi ý:

# Sử dụng set() để lưu trữ các giá trị không bị trùng lặp.
# Code mẫu:
a = [12,24,35,24,88,120,155,88,120,155]
print(set(a))
def xoaTrung( li ):
    list_moi=[]
    xem = set()
    for i in li:
        if i not in xem:
            xem.add( i )
            list_moi.append(i)
            # Code by Quantrimang.com
    return list_moi

li=[12,12,15,24,35,35,24,88,120,155,88,120,155]
print ("List sau khi xóa giá trị trùng là:",xoaTrung(li))




