# -*- coding: utf-8 -*-

# %% LIST
my_List = [10, 20, 30, 40]
type(my_List)

my_List[0] = 50
print(my_List)

my_List.append(60) # add extra data
print(my_List)

my_List.pop() #remove last character of list
print(my_List)

my_List.remove(20)#remove 20
print(my_List)

counter = my_List.count(30)#number of pieces of 30
print(counter)

string_list = ["Ali", "Mehmet", "Veli"]
string_list2 =  ["Umut", "Halit", "Mahmut"]
print(string_list[0])

string_list[0] = "C"
print(string_list)

string_list3 = string_list + string_list2
print(string_list3)

string_list3 = string_list3 * 2 
print(string_list3)

string_list3.reverse()
print(string_list3)

mix_list = [10, 20, "A", "B"]
print(mix_list[1] , mix_list[2])

nested_list = [1, 2, "Ali", [3, ["Veli"]]]
print(nested_list[2], nested_list[3])

character = nested_list[3][1]
print(character)

divided_list = nested_list[:3]
print(divided_list)

# %% DICTIONARY
foods = {"Apple" : 100, "Orange" : 200, "Banana" : 300}# keyword and their answers
print(foods["Apple"])

foods["Orange"] = 300
print(foods["Orange"])

foodsCalorie = {100 :"Apple", 200 : "Orange" , 300 : "Banana"}
print(foodsCalorie[100])

# %% SET 

list1 = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,5,6,4,6,5,4,1,2,3,5,4,7]
list1_set = set(list1) 
print(list1_set)

my_set = {"a", "b", "c", "a"}
print(my_set)

# %% TUPLE
my_tuple = (1, 2, "Ali", 6.5) #it same as list but it's unchangeable
print(my_tuple[2])

#my_tuple[1] = "A" -> ERROR

# %% COMMON FUNCTIONS FOR DATA:  RANGE ENUMERATE RANDOM SHUFFLE MAP FILTER LAMBDA

print(list(range(10)))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(0, 22, 2)))#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for (index, num) in enumerate(list(range(5, 15))):#enumerate match index and characters
    print(f"index: {index}   num: {num} ")

from random import randint, shuffle # shuffle: random change values

print(randint(0, 100))# 0-100 random value

new_list = []
for i in list(range(5)):
    new_list.append(i/2)
print(new_list)
#list(map(divide, list(range(5)))) it same as above result

def control(string):
    return "a" in string
print(control("Selam"))
str_list =["ali", "Mehmet", "Veli"]
rslt_list = list(map(control, str_list))#you can use two process in that function
print(rslt_list)


print(list(filter(control, str_list)))#getting that word "ali"

multp = lambda number : number *3#writing functions one line

print(multp(3))