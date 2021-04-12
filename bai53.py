# Yêu cầu:

# Định nghĩa một class có tên là Circle có thể được xây dựng từ bán kính. Circle có một method có thể tính diện tích.

# Gợi ý:

# Sử dụng def methodName(self) để định nghĩa method.

class Circle:
    def __init__(self,r) -> None:
        self.r = r 
    def dienTich(self):
        return round(3.14*self.r*self.r,2)

a = Circle(2)
print(a.dienTich())
        
