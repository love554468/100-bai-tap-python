# Câu hỏi:

# Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.

# Ví dụ đầu vào là: 0100,0011,1010,1001

# Đầu ra sẽ là: 1010

list_bit_num = [x for x in input().split(",")]
# print(list_bit_num)
list_store = [];
for x in list_bit_num:
    # if(int(x,2)%5==0):
    if not int(x,2)%5:
        list_store.append(x)
print(",".join(list_store))
