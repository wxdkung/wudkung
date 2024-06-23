"""
# Part: Python Conditions
#
"""

a = 200
b = 500

if a > b:
    print("a > b is true.")
elif a < b:
    print("a < b is true1.")
    print("a < b is true1.1")
    print("a < b is true1.2")
elif a <= b:
    print("a < b is true2.")
elif a == b:
    print("a < b is true3.")
else:
    print("Nothing.")

if a < b : print("a < b is True.")

print("B") if a < b else print("A")

a = 200
b = 30
c = 500
if (a > b) and (c > a):
    print("Both is True.")
if (a > b) or (a > c):
    print("some cond is True")
if not a > b:
    print("Not")
if b > a:
    print("pass")
    pass

x = 50
if x > 10 :
    print("Let's go!")
    if x > 20:
        print("x > 20 is True1")
        if x > 20:
            print("x > 20 is True2")
            if x > 20:
                print("x > 20 is True3")
    else:
        print("x > 20 is False")