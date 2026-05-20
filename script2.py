# BÀI 1
n = int(input("Nhap so: "))

if n % 2 == 0:
    print("Chan")
else:
    print("Le")

# BÀI 2
w = int(input("Nhap W: "))
h = int(input("Nhap H: "))

print("Dien tich S=", w * h)

# BÀI 3
n = int(input("Nhap n: "))

for i in range(n, 0, -1):
    print(i)

# BÀI 4
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))

if a == 0:
    if b == 0:
        print("Vo so nghiem")
    else:
        print("Vo nghiem")
else:
    print("x =", -b / a)

# Bài 5
a = [1, 5, 3, 9, 2]

max_value = a[0]

for i in a:
    if i > max_value:
        max_value = i

print("Max =", max_value)

# Bài 6
n = int(input("Nhap so 1-7: "))

match n:
    case 1:
        print("Chu Nhat")
    case 2:
        print("Thu Hai")
    case 3:
        print("Thu Ba")
    case 4:
        print("Thu Tu")
    case 5:
        print("Thu Nam")
    case 6:
        print("Thu Sau")
    case 7:
        print("Thu Bay")
    case _:
        print("Khong hop le")

# BÀI 7
n = int(input("Nhap n: "))

s = 0

for i in range(1, n + 1):
    s += i

print("Tong =", s)


