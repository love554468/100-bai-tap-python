# Viết chương trình tạo ngẫu nhiên list gồm 5 số chẵn nằm trong đoạn [100;200]


import random
print(random.sample([i for i in range(100,201) if not i%2],5))