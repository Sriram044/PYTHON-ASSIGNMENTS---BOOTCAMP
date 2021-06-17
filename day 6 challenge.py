#1) Write a Python script to merge two Python dictionaries

num1={'x': 100,'y':200}
num2={'z': 200, 'a':100}
c=num1.copy()
c.update(num2)
print('merge two python dictionaries')
print(c)

#2) Write a Python program to remove a key from a dictionary

num2.pop('z')
print('remove a key from dictionaries')
print(num2)

#3) Write a Python program to map two lists into a dictionary

keys =['x','y','z','a']
values=[100,200,200,100]
mapp=dict(zip(keys,values))
print("mapp two list into dictionary")
print(mapp)

#4) Write a Python program to find the length of a set

CSK = {"dhoni", "bravo", "jadeja"}
print("length is",len(CSK))

#5)# Write a Python program to remove the intersection of a 2nd set from the 1st set

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("\nRemove the intersection of a 2nd set from the 1st set ")
sn1-=sn2
print("sn1: ",sn1)
print("sn2: ",sn2)
