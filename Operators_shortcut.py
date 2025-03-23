# +=
x = 5 
x += 3  # เท่ากับ x = x + 3
print(x)  # ผลลัพธ์คือ 8

x = "Hello"  #string
x += " World"  # เท่ากับ x = x + " World"
print(x)  # ผลลัพธ์คือ "Hello World"

x = [1, 2, 3] #list
x += [4, 5]  # เท่ากับ x = x + [4, 5]
print(x)  # ผลลัพธ์คือ [1, 2, 3, 4, 5]


# -=
x = 10
x -= 4  # เท่ากับ x = x - 4
print(x)  # ผลลัพธ์คือ 6

x = "Hello World" #string
x -= " World"  # แต่การใช้ -= กับสตริงใน Python จะทำให้เกิดข้อผิดพลาด
print(x)  # Error: unsupported operand type(s) for -=: 'str' and 'str'

x = [1, 2, 3, 4] # (List)
x -= [2, 3]  # จะลบค่าที่มีในลิสต์ที่กำหนดออกจาก x
print(x)  # ผลลัพธ์คือ [1, 4]