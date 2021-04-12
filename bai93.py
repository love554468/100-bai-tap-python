# Yêu cầu:

# Định nghĩa class Nguoi và 2 class con của nó: Nam, Nu. Tất cả các class có method "getGender" có thể in "Nam" cho class Nam và "Nữ" cho class Nu.

# Gợi ý:

# Sử dụng Subclass(Parentclass) để định nghĩa 1 class con.
# Code mẫu:

class Nguoi:
    def getGender(self):
        self.gender = "Unknow"

class Nam(Nguoi):
    def getGender(self):
        self.gender = "Nam"

class Nu(Nguoi):
    def getGender(self):
        self.gender = "Nu"

a = Nguoi()
b = Nam()
c = Nu()

print(a.gender)
print(b.gender)
print(c.gender)

# class Nguoi(object):
#     def getGender(self):
#         return "Unknown"

# class Nam(Nguoi):
#     def getGender(self):
#         return "Nam"
# # Code by Quantrimang.com
# class Nu(Nguoi):
#     def getGender(self):
#         return "Nữ"

# aNam = Nam()
# aNu= Nu()
# print (aNam.getGender())
# print (aNu.getGender())