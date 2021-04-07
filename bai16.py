# Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. Giả sử đầu vào sau được cấp cho chương trình: hello world! 123

# Thì đầu ra sẽ là:

# Số chữ cái là: 10
# Số chữ số là: 3

str = input("Nhap 1 cau : ")
d = {"Chuso":0,"Chucai":0}

for s in str:
    if s.isdigit():
        d["Chuso"]+=1
    if s.isalpha():
        d["Chucai"]+=1
print("so chu so: %s " %(d["Chuso"]))
print("so chu cai: %s " %(d["Chucai"]))