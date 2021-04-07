tong = 0;

while True:
    s = input()
    if not s:
        break
    intp = s.split()
    if intp[0] == "D":
        tong+=int(intp[1])
    elif intp[0] == "W":
        tong-=int(intp[1])
    else:
        pass
print("tong la ", tong)