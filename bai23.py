# def putNumbers(n):
#     i = 0
#     while i<n:
#         j=i
#         i=i+1
#         if j%7==0:
#             yield j
# # Bài tập Python 23 Code by Quantrimang.com
# for i in putNumbers (100):
#      print (i)

# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length - 1,-1,-1):
#         yield my_str[i]

# # Vòng lặp for đảo ngược chuỗi
# # Viết bởi Quantrimang.com
# # Output:
# # o
# # l
# # l
# # e
# # h
# for char in rev_str("hello"):
#      print(char)

# ===== tự làm thôi nào

# Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7.

def sol(n):
    i = 0
    while i<n:
        j=i 
        i+=1
        if not j%7:
            yield j 

for i in sol(int(input())):
    print(i)
