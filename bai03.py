# x = int(input("Nhap n: "))

# j = []

# for i in range(1,x+1):
#     j.append(str(i))
#     j.append(":")
#     j.append(str(i*i))
#     j.append(",")
# k = "{" + "".join(j) + "}"

# print(k)

n = int(input("Nhap vao 1 so: "))
d = dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)
