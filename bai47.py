# Viết chương trình Python dùng map() và filter() để tạo list chứa giá trị bình phương của các số chẵn trong [1,2,3,4,5,6,7,8,9,10].

def sol():
    a = list(map(lambda x: x**2, [1,2,3,4,5,6,7,8,9,10]))
    b = list(filter(lambda x:x%2==0,a))
    print(b)

sol()