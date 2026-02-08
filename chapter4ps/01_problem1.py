fruits=[]
f1=input("enter fruit 1: ")
fruits.append(f1)

f2=input("enter fruit 2: ")
fruits.append(f2)

f3=input("enter fruit 3: ")
fruits.append(f3)

f4=input("enter fruit 4: ")
fruits.append(f4)

f5=input("enter fruit 5: ")
fruits.append(f5)

f6=input("enter fruit 6: ")
fruits.append(f6)

f7=input("enter fruit 7: ")
fruits.append(f7)





friends=[]


fr1=input("enterr friend 1: ")
friends.append(fr1)

fr2=input("enterr friend 2: ")
friends.append(fr2)

fr3=input("enterr friend 3: ")
friends.append(fr3)

fr4=input("enterr friend 4: ")
friends.append(fr4)

fruits.extend(friends)
fruits.insert(7,"papita")

print(fruits)