"""
#
# Part: Python Operators
# Arithmetic Operators
#
"""

x = 4 + 5
print(x)

x = 4
y = 5
z = x + y + 1
print(z)

z = x / y
v = x % y
print(z, v)

"""
#
# Part: Python Operators
# Assignment Operators
#
"""
a = 1
a += 5
# a = a + 5
print(a)

"""
#
# Part: Python Operators
# Comparison Operators
#
"""

a = 10 
b = 15
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

"""
#
# Part: Python Operators
# Logical Operators
#
"""

a = 10
b = 15
print((a < 5) & (b > 20)) # & และ
print((a == 10) | (a <= 9)) # | หรือ
print( not (a == 10) | (a <= 9))