from operator import itemgetter, attrgetter
list1 = []

while True:
    s = input()
    if not s:
        break
    # tup = s.split(",")
    # tuple1 = (tup[0],tup[1],tup[2])
    tup = (s.split(","))
    list1.append(tuple1)

print(sorted(list1, key=itemgetter(0,1,2)))