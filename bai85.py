# Yêu cầu:

# Viết chương trình in list sau khi xóa các số chẵn trong [5,6,77,45,22,12,24].

# Gợi ý:

# Sử dụng list comprehension để xóa một loạt phần tử của list.
# Code mẫu:

lst = [5,6,77,45,22,12,24]

new_list = [i for i in lst if i%2]
print(lst)
print(new_list)