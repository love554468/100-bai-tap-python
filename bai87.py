# Yêu cầu:

# Viết chương trình in list sau khi đã xóa số thứ 0, thứ 2, thứ 4, thứ 6 trong [12,24,35,70,88,120,155].

# Gợi ý:

# Sử dụng list comprehension để xóa một loạt phần tử trong list.
# Sử dụng hàm enumerate() để lấy index, value của tuple.

# lst = [12,24,35,70,88,120,155]

# for index,value in enumerate(lst):
#     if index == 0 or index == 2 or index == 4 or index == 6:
#         lst.remove(lst[index])

# print(lst)

# good
lst = [12,24,35,70,88,120,155]

print([x for i,x in enumerate(lst) if i%2])
