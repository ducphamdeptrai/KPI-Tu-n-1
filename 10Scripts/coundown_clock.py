import time

n = int(input("Đếm ngược bao nhiêu giây: "))
while n > 0:
    print(n, "giây")
    time.sleep(1)
    n -= 1
print("Hết giờ!")
