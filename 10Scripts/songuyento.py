n = int(input("Nhập số: "))
if n < 2:
    print("Không phải số nguyên tố")
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Không phải số nguyên tố")
            break
    else:
        print("Là số nguyên tố")
