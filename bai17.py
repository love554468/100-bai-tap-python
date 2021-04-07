string = "Nguyen DInh Binh"
demHoa = 0
demThuong = 0
for s in string:
    if s.isupper():
        demHoa +=1
    if s.islower():
        demThuong +=1
print("Chu hoa: {0} Chu thuong: {1}".format(demHoa,demThuong))
