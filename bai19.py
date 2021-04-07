# list1 = []
# for x in range(1,10):
#     list1.append(x)

# new_list = []

# for x in list1:
#     if x%2:
#         new_list.append(x)

# print(new_list)

list1 = input("Nhap mot danh sach: ")
new_list = [x for x in list1.split(",") if int(x)%2]
print(",".join(new_list))

