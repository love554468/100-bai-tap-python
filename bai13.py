# list_str = [x for x in input().split()]
# # print(list_str)
# set_list = set(list_str)
# # print(set_list)
# a=list(set_list)
# a.sort()
# # print(a)
# str = ""
# for x in a:
#     str+=x + " "
# print(str)

# # viet lai nay
# new_list = list(set([x for x in input().split()]))
# a = new_list.sort()
# # str = ""
# # for i in a:
# #     str = str + i + " "

# print(a)

# code loi giai hay ghe
s = input("Nhập chuỗi của bạn: ")
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))

