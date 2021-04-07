# j = []
# for i in range(5):
#     k = int(input("Nhap vao: "))
#     j.append(str(k))

# x = ",".join(j);
# print(x)

values = input("Nhap vao cac gia tri: ")
l = values.split(",")
t = tuple(l)
print(l)
print(t)