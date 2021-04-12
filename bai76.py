# Vui lòng viết chương trình để xuất một số ngẫu nhiên, chia hết 
# cho 5 và 7, từ 0 đến 200 (gồm cả 0 và 200), sử dụng module random và list comprehension.

# Gợi ý:

# Giống bài 75.

import random

print(random.choice([i for i in range(201) if (not i%5 and not i%7)]))

