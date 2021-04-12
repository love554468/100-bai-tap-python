# Yêu cầu:

# Viết hàm tìm kiếm nhị phân để tìm các item trong một list đã 
# được sắp xếp. Hàm sẽ trả lại chỉ số của phần tử được tìm thấy trong list.

# Gợi ý:

# Sử dụng if/elif để giải quyết các điều kiện.

import math

def bin_search(li,element):
    bottom = 0 
    top = len(li) -1
    index = -1
    while top>= bottom and index == -1:
        mid = int(math.floor((top + bottom)/2.0))
        if li[mid]  == element:
            index = mid
        elif li[mid] <element:
            bottom = mid +1
        else:
            top = mid -1
    return index 

li=[2,5,7,9,11,17,222]
print (bin_search(li,11))
print (bin_search(li,12))