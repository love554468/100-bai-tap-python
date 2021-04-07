nhap_chuoi = input("nhap chuoi:")
# print(type(nhap_chuoi))
list_str = nhap_chuoi.split(",")
# print(list_str)
list_str.sort()
# print(list_str)
str = ",".join(list_str)
print(str)
# code cua tac gia

# items=[x for x in input("Nhập một chuỗi: ").split(',')]
# items.sort()
# print (','.join(items))
