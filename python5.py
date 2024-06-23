"""
#
# Part: python While Loop
#
"""
i = 1
while i < 5:
    print("i =" , i)
    i+=1

i = 1
while i < 5:
    print("i =", i)
    if i == 3:
        break #หยุดพอแค่นี้
    # cotinue ทำต่อ (ระวังคอมพัง)
    i+=1

i = 1
while i < 5:
    print("i =" , i)
    i+=1
else:
    print("Game Over")

"""
#
# Part: python For Loop
#
"""

fruits = ["Apple", "Banana", "Coconut"]
for fruit in fruits:
    print("Fruit:", fruit)

for fruit in fruits:
    print("Fruit:", fruit)
    if fruit == "Banana":
        break

for fruit in fruits:
    if fruit == "Banana":
        break
    print("Fruit:", fruit)

##########################################

for fruit in fruits:
    if fruit == "Banana":
        continue
    print("Fruit:", fruit)

for x in range(len(fruits)+1):
    print("Number =", x)

for x in range(5):
    print("Number =", x)
else:
    print("Game Over")

adjs = ["Red", "Yellow", "Brown"]
fruits = ["Apple", "Banana", "Coconut"]
for adj in adjs:
    for fruit in fruits:
        print(adj, fruit)