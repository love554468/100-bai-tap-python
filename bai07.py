class bai7(object):
    def __init__(self) -> None:
        super().__init__()
        self.s = 0;

    def calBP(self):
        self.s = int(input("nhap so: "))
        return self.s**2

intObj = bai7()
k = intObj.calBP()
print(k)