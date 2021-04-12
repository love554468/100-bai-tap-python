# Định nghĩa một class có tên là Vietnam, với static method là printNationality.

# Gợi ý:

# Sử dụng @staticmethod để định nghĩa class với static method.

class Vietnam:
    @staticmethod
    def printNationality():
        return "Viet Nam!"


a = Vietnam()
print(a.printNationality())