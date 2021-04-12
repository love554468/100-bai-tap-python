# Yêu cầu:

# Viết chương trình để giải 1 câu đố cổ của Trung Quốc: Một trang trại thỏ và gà có 35 đầu, 94 chân, hỏi số thỏ và gà là bao nhiêu?

# Gợi ý:

# Sử dụng vòng lặp for để lặp qua tất cả các giả thuyết có thể.
# Code mẫu:

def giai(dau,chan):
    klg='Không có dáp án phù hợp!'
    for i in range(dau+1):
        j=dau-i
        if 2*i+4*j==chan:
            return i,j
    return klg
# Code by Quantrimang.com
dau=35
chan=94
dap_an=giai(dau,chan)
print (dap_an)