# Định nghĩa một class có tên là Shape và class con là Square. Square có hàm init để lấy đối số là chiều dài. Cả 2 class đều
#  có hàm area để in diện tích của hình, diện tích mặc định của Shape là 0.

# Gợi ý:

# Để ghi đè một method trong super class, chúng ta có thể định nghĩa một method có cùng tên trong super class.

# class Shape:

minh thay bai nay no ra de vo van hoac dijch linh tinh nen thoi ko lamf

class Shape(object):
    def __init__(self):
       pass

    def area(self):
       return 0
# Bài Python 54, Code by Quantrimang.com
class Square(Shape):
    def __init__(self, l):
       Shape.__init__(self)
       self.length = l

    def area(self):
       return self.length*self.length

aSquare= Square(3)
print (aSquare.area())
