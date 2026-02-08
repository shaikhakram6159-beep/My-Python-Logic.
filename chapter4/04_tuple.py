#tuple-->

a=(1,3,4,5,6,7,8,9,"akram", True, False)
print(a)
print(type(a))


#Tuple Methods-->
n=a.count(5)
print(n)
n=a.index(8)
print(n)

#concatenation in tuple-->

a=(1,2,3,4,5)
b=(6,7,8,9,0)
print(a+b)

repeated=a*2#this * symbol are used to repeat the tuple
repeated=b*1
print(repeated)
print(repeated)

print( 2 in a)#True
print(4 in b)#False

#sicing in tuple-->
print(a[0:4])
print(b[0:2])
