# Viết một chương trình để tạo tất cả các câu có chủ ngữ nằm trong ["Anh","Em"], động từ nằm trong ["Chơi","Yêu"] và tân ngữ là ["Bóng đá","Xếp hình"].

# Gợi ý:

# Sử dụng list[index] để lấy phần tử từ list.

def sol():
    for i in ["Anh","Em"]:
        for j in ["Chơi","Yêu"]:
            for k in ["Bóng đá","Xếp hình"]:
                print("%s %s %s"%(i,j,k))



sol()