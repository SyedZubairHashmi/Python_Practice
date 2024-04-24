print("for loop while loop and do while loop")

for i in range(10):
    print(i)

for i in range(10):
    print("*")    

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(0, 30, 3):
  print(x)

print("print payramid by for loop")
for i in range(5):
   for j in range(i+1):
        print("*", end=" ")
   print()

print("print reverse payramid")
for i in range(5,0,-1):
   for j in range(i):
        print("*",end=" ")

   print()

print("Now form here we practice while loop")

i=0
while i < 10:
   print(i)
   i+=1


print("it print till 3")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1