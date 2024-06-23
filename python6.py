"""
#
# Part: python Function
#
"""

def my_function():
    print("Hello World1")
    print("Hello World2")

my_function()

# parameter
def my_name(fname):
    print("My name is ", fname)

my_name("Anya")

def my_name2(fname, lname):
    print("My name is ", fname, lname)

my_name2("Anya", "Roger")
my_name2(lname= "Anya", fname= "Roger")#แบบระบุ สามารถสลับตำแหน่งได้

def my_name3(lname = "Roger"): ## ค่า default
    print("My last name is ", lname)

my_name3()
my_name3("Paul")

def my_fruits(fruits):
    for fruit in fruits:
        print(fruit)

fruits = ["Apple", "Banana", "Coconut"]
my_fruits(fruits)

def red_potion(hp):
    return hp + 50

print("HP: ", red_potion(100))
print("HP: ", red_potion(70))