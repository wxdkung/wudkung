# สร้างลิสต์ของจำนวนเต็มตั้งแต่ 1 ถึง 20
numbers = list(range(1, 21))

# ใช้ list comprehension เพื่อแยกจำนวนคี่และจำนวนคู่
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# แสดงผลลัพธ์
print("จำนวนคู่:", even_numbers)
print("จำนวนคี่:", odd_numbers)
