"""
# Part: Python Collections
#List, Tuple, Set and Dictionary
#
"""

"""
#
# Part: Python list
#
"""
this_list = ["apple", "banana", "coconut", "apple", "banana"]
print(this_list)
print(type(this_list))  # ประเภท
print(len(this_list))  # จำนวนในลิสต์
print(this_list[0])  # ตำแหน่ง นับจาก0

this_list.append("Cherry")  # เพิ่ม
print(this_list, len(this_list))
this_list.insert(1, "orange")
print(this_list, len(this_list))

this_list2 = ["apple", "banana", "coconut", "apple", "banana"]
this_list3 = ["mango", "pineapple", "grape"]
this_list2.extend(this_list3)  # ต่อกัน
print(this_list2, len(this_list2))

this_list4 = ["apple", "banana", "coconut", "apple", "banana"]
this_list4.remove("banana")  # ลบ
print(this_list4, len(this_list4))

this_list5 = ["apple", "banana", "coconut", "apple", "banana"]
this_list5.pop(1)
print(this_list5, len(this_list5))

this_list6 = ["apple", "banana", "coconut", "apple", "banana"]
del this_list6[1]  # ลบ
print(this_list6, len(this_list6))

this_list6.clear()
print(this_list6, len(this_list6))

del this_list5
# print(this_list5, len(this_list5))ลบเคื้อม1

this_list7 = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list7.sort()
print(this_list7, len(this_list7))
this_list8 = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list8.reverse()
print(this_list8, len(this_list8))

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

"""
#
# Part: Python Tuple
#
"""

this_tuple = ("apple", "banana", "coconut")
print(this_tuple)
print(type(this_tuple))
print(len(this_tuple))
print((this_tuple[2]))

this_tuple2 = ("apple", "banana", "coconut")
this_tuple3_list = list(this_tuple2)
print(this_tuple3_list)
print(type(this_tuple3_list))
this_tuple4 = tuple(this_tuple3_list)
print(this_tuple4)
print(type(this_tuple4))

this_tuple5 = ("apple", "banana", "coconut")
this_tuple6_list = list(this_tuple5)
this_tuple6_list.append("mango")
this_tuple7 = tuple(this_tuple6_list)
print(this_tuple7)
print(type(this_tuple7))

this_tuple8 = ("apple", "banana", "coconut")
this_tuple9_list = list(this_tuple8)
this_tuple9_list.remove("banana")
this_tuple10 = tuple(this_tuple9_list)
print(this_tuple10)
print(type(this_tuple10))

del this_tuple10
# print(this_tuple10)

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

"""
#
# Part: Python Set
#
"""

this_set = {"apple", "banana", "coconut"}
print(this_set)
print(type(this_set))
print(len(this_set))

for x in this_set:
    print(x)

    print("banana" in this_set)

    this_set2 = {"apple", "banana", "coconut"}
    this_set2.add("orange")
    print(this_set2, len(this_set2))
    this_set2.remove("apple")
    print(this_set2, len(this_set2))

    this_set3 = {"apple", "banana", "coconut"}
    this_set4 = {"pineapple", "grape"}
    this_set3.update(this_set4)
    print(this_set3, len(this_set3))

    # Union
    this_set5 = {"apple", "banana", "coconut"}
    this_set6 = {"pineapple", "grape"}
    this_set7 = {1, 2, 3}
    this_set8 = this_set5 | this_set6 | this_set7
    print(this_set8, len(this_set8))

    this_set8.clear()
    print(this_set8, len(this_set8))
    del this_set8
    # print(this_set8, len(this_set8))

"""
#
# Part: Python Dictionary
#
"""

this_dict={
    "brand": "Ford",
    "model": "Rapter",
    "year" : "2023"
}

print(this_dict)
print(type(this_dict))
print(len(this_dict))
print(this_dict["brand"])
print(this_dict.get("year"))
print(this_dict.keys())

this_dict["year"] = 2020
print(this_dict)
this_dict.update({"year": 2020})
print(this_dict)

this_dict["color"] = "red"
print(this_dict)

del this_dict["year"]
print(this_dict)

this_dict.clear()
print(this_dict, len(this_dict))
del this_dict
#print(this_dict)

this_dict2={
    "brand": "Ford",
    "model": "Rapter",
    "year" : "2023"
}

this_dict3={
    "brand": "Honda",
    "model": "Civic",
    "year" : "2019"
}

this_dict4={
    "brand": "Toyota",
    "model": "Colora",
    "year" : "2017"
}

my_car= {
    "car1": this_dict2,
    "car2": this_dict3,
    "car3": this_dict4
}
print(my_car ,len(my_car))
print(my_car["car2"]["model"])