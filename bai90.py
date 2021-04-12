# Yêu cầu:

# Viết chương trình in list sau khi đã xóa giá trị 24 trong [12,24,35,24,88,120,155].

# a = [12,24,35,24,88,120,155]
# a = a.remove(24)
# print(a)

a = [12,24,35,24,88,120,155]

print([x for x in a if x!=24])