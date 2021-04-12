# Yêu cầu:

# Viết chương trình đếm và in số ký tự của chuỗi do người dùng nhập vào.

# Ví dụ:

# Nếu chuỗi nhập vào là quantrimang.com thì đầu ra sẽ là:

# q,1
# u,1
# a,2
# n,2
# t,1
# r,1
# i,1
# m,2
# g,1
# .,1
# c,1
# o,1

# Gợi ý:

# Sử dụng dict để lưu trữ các cặp key/value.
# Sử dụng dict.get() để tra cứu key với giá trị mặc định.

str = input()

dic = dict()

for i in str:
    dic[i] = 0
for i in str:
    dic[i] +=1

for i,x in enumerate(dic):
    print(x,i)

# dic = {}
# chuoi=input("Nhập chuỗi cần đếm ký tự: ")
# # Code by Quantrimang.com
# for c in chuoi:
#     dic[c] = dic.get(c,0)+1
# print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))