# Viết chương trình để tạo ngẫu nhiên một list gồm 5 số, chia hết cho 5 và 7, nằm trong đoạn [1;1000].

import random

print(random.sample([i for i in range(1,1001) if not i%7 and not i%5],5))