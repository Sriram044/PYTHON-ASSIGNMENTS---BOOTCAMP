#1)	Write a program to create a list of n integer values and do the following
•	Add an item in to the list (using function)
•	Delete (using function)
•	Store the largest number from the list to a variable
•	Store the Smallest number from the list to a variable

list1=[20,2,3,4,5,6]
list2=[8,9,10]
list1.append(7)
list1.extend(list2)
list1.insert(4,5)
del list1[4]
k=list1.pop(6)
list1.remove(2)
a=max(list1)
A=min(list1)
print(list1)
b=sorted(list1)
print(k)
print(a)
print(A)
print(b)
# 2) Create a tuple and print the reverse of the created tuple

x=(1,2,3,4)
y=reversed(x)
print(tuple(y))

#3)Create a tuple and convert tuple into list
sri=(1,2,3,4)
z=list(sri)
print(z)
