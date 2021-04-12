# Viết chương trình xuất ra một số chẵn ngẫu nhiên trong khoảng 0 đến 10 (bao gồm cả 0 và 10), sử dụng module random và list comprehension.

# Gợi ý:

# Sử dụng random.choice() để tạo một phần tử ngẫu nhiên từ list.


import random
print(random.choice([i for i in range(11) if not i%2]))