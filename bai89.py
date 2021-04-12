# Yêu cầu:

# Viết chương trình in list sau khi đã xóa số ở vị trí thứ 0, thứ 5, thứ 5 trong [12,24,35,70,88,120,155].

a = [12,24,35,70,88,120,155]

print([x for i,x in enumerate(a) if (i!=5 and i!=0)])