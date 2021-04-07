# // 
# x = range(2000,3201)
# for n in x:
#     if((n%7)==0 and (n%5)!=0):
#         print(n);

#note
#range() no như một khoảng tóm gọn trong for của c++
#for(int i=0;i<n;i++) -> range(0,n), for i in range(0,n):

#python list append() method
# append() như là một phương thức nối mảng trong python rất hay 
# cái ý nghĩa append là nối thêm

#ép kiểu trong python type(variable)

# mydb = {"hellu","hi","hallo"}
# x = "#".join(mydb)
# print(x)

j = []
for i in range(2000,3201):
    if((i%7)==0 and (i%5)):
        j.append(str(i))
k = ",".join(j)
print(type(k))