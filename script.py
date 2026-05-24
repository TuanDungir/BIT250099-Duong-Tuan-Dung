# =========================
# BÀI 1
# Kiểm tra số chẵn
# =========================

def is_even(n):
    return n % 2 == 0

so = int(input("Nhập số: "))

if is_even(so):
    print("Là số chẵn")
else:
    print("Không phải số chẵn")


# =========================
# BÀI 2
# Tìm số lớn nhất trong 3 số
# =========================

a = int(input("\nNhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

print("Số lớn nhất là:", max(a, b, c))


# =========================
# BÀI 3
# Hàm với đối số mặc định
# =========================

def greet(name="Student"):
    print("Hello,", name + "!")

print()
greet()
greet("Dũng")


# =========================
# BÀI 4
# Kiểm tra tuổi hợp lệ
# =========================

tuoi = int(input("\nNhập tuổi: "))

if 1 <= tuoi <= 120:
    print("Tuổi hợp lệ")
else:
    print("Tuổi không hợp lệ")


# =========================
# BÀI 5
# Đếm số lần xuất hiện của 'a'
# =========================

chuoi = input("\nNhập chuỗi: ")

print("Số lần xuất hiện của 'a':", chuoi.count('a'))


# =========================
# BÀI 6
# Chuyển độ C sang độ F
# =========================

c = float(input("\nNhập nhiệt độ C: "))

f = c * 9 / 5 + 32

print(f"Nhiệt độ F là: {f:.2f}")


# =========================
# BÀI 7
# Tính BMI
# =========================

weight = float(input("\nNhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

bmi = weight / (height * height)

print(f"BMI của bạn là: {bmi:.2f}")


# =========================
# BÀI 8
# Phép chia có xử lý lỗi
# =========================

try:
    x = int(input("\nNhập số thứ nhất: "))
    y = int(input("Nhập số thứ hai: "))

    print("Kết quả:", x / y)

except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0")

except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên")


# =========================
# BÀI 9
# Tính căn bậc hai
# =========================

import math

n = float(input("\nNhập số: "))

if n < 0:
    print("Không thể tính căn bậc hai của số âm")
else:
    print("Căn bậc hai là:", round(math.sqrt(n), 2))


# =========================
# BÀI 10
# Thông tin 3 sinh viên
# =========================

for i in range(1, 4):
    print(f"\n--- Sinh viên {i} ---")

    ten = input("Nhập tên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))

    dtb = (toan + ly + hoa) / 3

    print("Tên:", ten)
    print("Điểm trung bình:", round(dtb, 2))
    