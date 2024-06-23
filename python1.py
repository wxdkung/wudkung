# Part : Python comment

# This is a comment
# Writting
print("Hello World 1")

""" 
This is a comment
Writting
"""

print("Hello World 2")

# Part : Python Variables

x = 5
y = "Hello Bro"

print(x, y)

x = str(3)
y = int(3)
z = float(3)
print(type(x), type(y), type(z))

# Part : Python Variables Name

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
MY_VAR = "John"
"""
# 2myvar = "John" Fail name 
# my-var = "John" Fail name 
# my var = "John" Fail name 
"""
# Camel Case 
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"

# Part : Python Variables String

x = "Hey Bro"
print(x)

y = """
1 Hey Bro
2 Hey Bro
3 Hey Bro
4 Hey Bro
5 Hey Bro
"""
print(y)

x = "Hey Bro"
print(x[6])
print(len(x))

print("Hey" in x)
print("Whatsup" not in x)

# Fail Check 
print("Whatsup" in x) 

print(x.upper()) # พิมพ์ใหญ่
print(x.lower()) # พิมพ์เล็ก
print(x.replace("Bro", "Sis"))  # แทนที่คำ
print(x.split(" ")) # แบ่งข้อความ

a = "Apple"
b = "Banana"
print(a + " " + b) # รวมคำ 

price = 20
word = f"Price: {price:.2f}"
print(word)