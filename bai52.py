# Định nghĩa class có tên là Hinhchunhat được xây dựng bằng chiều dài và chiều rộng. Class Hinhchunhat có method để tính diện tích.

# Gợi ý:

# Như bài 52.
class Hinhchunhat:
    def __init__(self,d,r) -> None:
        self.d = d
        self.r = r 
    def dien_tich(self):
        return self.d*self.r 

a = Hinhchunhat(3,4)
print(a.dien_tich())