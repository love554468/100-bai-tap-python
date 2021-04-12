# Yêu cầu:

# Sử dụng list comprehension để viết chương trình in list sau khi đã loại bỏ các số chia hết cho 5 và 7 trong [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]

print([i for i in lst if i%5 and i%7])
