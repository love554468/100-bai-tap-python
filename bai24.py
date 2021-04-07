# - cho nguoi dung nhap den 4 thi nghi
# - so sanh va nhap tinh 2 bien x,y 
# - tinh kc = ct khoang cach cho 2 bien xy 

import math
x = 0
y = 0
while True:
    s = input()
    if s:
        listt = s.split()
        if listt[0] == 'UP':
            x+=int(listt[1])
        elif listt[0] == 'DOWN':
            x-=int(listt[1])
        elif listt[0] == 'LEFT':
            y-=int(listt[1])
        else:
            y+=int(listt[1])
    else:
        break
z = round(math.sqrt(x*x + y*y),2)
print(z)