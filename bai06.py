class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Nhap chuoi: ")
    
    def printString(self):
        print(self.s.upper())



# strObj = InputOutString()
# strObj.getString()
# strObj.printString()

class h(object):
    def __init__(self) -> None:
        super().__init__()
        self.a = "test"
    def printString(self):
        print(self.a.upper())

strH = h()
strH.printString() 
