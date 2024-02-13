my_list=["toyota","bmw","subaru","mitsubishi","mercedes"]
my_list.insert(3,"nissan")
print(my_list)
my_list.append("mitsubushi")
print(my_list)
print(my_list[0])
print(my_list[2])
print(my_list[3])
print(my_list[4])
my_list[1]="mercedes"
print(f"{my_list[1]} is manufactured in Germany")

print(type(my_list))

#tuple datastructure
my_tuple=("Apple","Banana","Cherry","Mango","Kiwi","Orange")
print(my_tuple)

#set datastructure
my_set=("red","green","blue","yellow","black")
print(my_set)

#dictionaries datastructure
my_dict={"name": "Leshan", "Age": 45,"Gender": "Male"}
print(my_dict["Age"])
print(my_dict["Gender"])