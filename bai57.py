# Yêu cầu:

# Định nghĩa một class exception tùy chỉnh, nhận một thông báo là thuộc tính.

# Gợi ý:

# Để định nghĩa một class exception tùy chỉnh, chúng ta phải định nghĩa một class kế thừa từ Exception.



class MyError(Exception):
    """This is document, my own exception class
    msg -- explanation of the error
    """

    def __init__(self, msg) -> None:
        self.msg = msg 
        self.test = "hihi"

error = MyError("Co gi do sai sai")
print(error)