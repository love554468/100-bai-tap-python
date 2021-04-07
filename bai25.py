# Câu hỏi:

# Viết chương trình tính tần suất các từ từ input. Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.

# Giả sử input là: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Thì output phải là:

# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được cung cấp cho câu hỏi, nó phải được giả định là một input được nhập từ giao diện điều khiển.

freq = {}
for i in input().split():
    freq[i] = freq.get(i,0) +1
words = sorted(freq.keys())
for w in words:
    print(w,freq[w])

