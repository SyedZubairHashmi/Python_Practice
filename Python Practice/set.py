print("Set are unorderd and not changeable ")
set1={"zubair","rehan","faheem","ibrahim","baddar","ishtiaq"}
set2={22,234,54,645,23}
print("we can not acces element of set by indexing because it is not in order so we dont now which value is at which index")
print(len(set1))
print("Adding in set by add method")
set1.add("umair")
print(set1)
print("To concate two sets by update methode")
set1.update(set2)
print(set1)
print("remove element form set")
set1.remove("umair")
print(set1)
print("do delte or clear or remove all at once so use clear method")
set1.clear()
print(set1,set2)