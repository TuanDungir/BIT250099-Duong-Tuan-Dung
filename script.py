# Bài 1
so_nguyen = 10
so_thuc = 3.14
chuoi = "Hello Python"

print("BÀI 1")
print("Số nguyên:", so_nguyen)
print("Số thực:", so_thuc)
print("Chuỗi:", chuoi)

# Bài 2
PI = 3.14
r = 5
chu_vi = 2 * PI * r

print("\nBÀI 2")
print("Chu vi hình tròn:", chu_vi)

# Bài 3
print("\nBÀI 3")
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

print("Tổng:", a + b)
print("Hiệu:", a - b)
print("Tích:", a * b)

if b != 0:
    print("Thương:", a / b)
else:
    print("Không thể chia cho 0")

# Bài 4
def sum_two_numbers(a, b):
    return a + b

print("\nBÀI 4")
print("Tổng của 7 và 8 là:", sum_two_numbers(7, 8))

# Bài 5
print("\nBÀI 5")

name = "Nguyen Van A"
age = 18
average_score = 8.5

print("Kiểu dữ liệu của name:", type(name))
print("Kiểu dữ liệu của age:", type(age))
print("Kiểu dữ liệu của average_score:", type(average_score))

age_next_year = age + 1
doubled_score = average_score * 2

print("Tên:", name)
print("Tuổi:", age)
print("Điểm trung bình:", average_score)
print("Tuổi năm sau:", age_next_year)
print("Điểm trung bình nhân đôi:", doubled_score)


