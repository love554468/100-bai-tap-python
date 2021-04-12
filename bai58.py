# Giả sử rằng chúng ta có vài địa chỉ email dạng username@companyname.com, hãy viết một chương trình để in username của địa chỉ email cụ thể.
#  Cả username và companyname chỉ bao gồm chữ cái.

# Ví dụ: Nếu cung cấp địa chỉ email QTM@quantrimang.com thì đầu ra sẽ là: QTM.

# Trong trường hợp dữ liệu đầu vào không có sẵn, ta giả định nó được người dùng nhập vào từ giao diện điều khiển.

# Gợi ý:

# Sử dụng \w để kiểm tra chữ cái
# s = input()
# s = s.split('@')
# print(s[0])

# import re 

# eMail = input()

# pat = "(\w)@(\w).(\w)"
# re1 = re.match(pat, eMail)
# print(re1.group(1))

import re
emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
re2 = re.match(pat2,emailAddress)
print (re2.group(2)) 
