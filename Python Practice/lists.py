print("list")


print("Lists  we can change list item when we creat list add and remove elements")

fruits = ["mango","orange","apple","banana","kiwi","grapes","tomato"]
list1 = [True,23,45,False,"zubair","faheem","ishtiaq"]
print("we can assign all type at once in list")
print(list1)
print(fruits)

print("indexing in listsame as in string")
print(fruits[:4])

if "apple" in fruits:
    print("yes 'apple' is present in fruits")

print("change list items")
fruits[0] = "cherry"
print(fruits[0])
fruits.append("football")
print(fruits)
fruits.insert(1,"cricket")
print(fruits)
fruits.extend(list1)
print(fruits)

fruits.remove("ishtiaq")
print(fruits)

print("clear, which empty the list and del [0] delete , and pop()/pop(3) also delete and remove this all method remove element frome list")

print("for loop throgh list")
for i in fruits:
    print(i)

print("we can also give range i for loop")
for i in range(len(fruits)):
    print(fruits[i])

print("while loop in list")
i=0
while i < len(fruits):
    print(fruits[i])
    i=i+1


print("make rwo list and increment or add element in 2 list")
citys = ["karachi","lahore","multan","quetta","tatta","tokyo"]
tcitys= []
for x in citys:
    if "t" in x:
        tcitys.append(x)

print(tcitys)

number = [10,34,534,634,2,42,34,2,4,5,6,1,0]
number.sort()
print("It print sorted list in ascending order")
print(number)
number.sort(reverse=True)
print("It print sorted list but in descending order")
print(number)
