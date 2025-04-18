import qrcode

data = input("Nhập dữ liệu để tạo mã QR: ")
img = qrcode.make(data)
img.save("qrcode.png")
print("Đã lưu mã QR thành 'qrcode.png'")
