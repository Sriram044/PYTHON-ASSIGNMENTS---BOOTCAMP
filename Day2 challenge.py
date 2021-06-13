'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Day2 challenge
# string practice

#How to print a string?
print("30 days 30 hour challenge")
print('30 days 30 hour challenge')

#Assigning string to variables

hours= "thirty"
print(hours) # output:thirty
name='sriram'
print(name) # output:sriram

#indexing using string
days='thirty days'
print(days[0]) # output: t
print(days[6]) # output: ''space
print(days[4]) # output: t
print(days[9]) # output: y

#How to print the particular character from certain text?
challenge = "i will win"
print(challenge[7:10]) #output: win 
name = 'sriram.d'
print(name[0:6])# output:sriram
print(name[0:7])# output:sriram.
print(name[0:9])# output:sriram.d 
print(name[3:6])# output:ram

#Length of the character
challenge= "i will win"
print(len(challenge))
name= 'sriram'
print(len(name))

#Convert string to lower character
challenge='I WILL WIN'
print(challenge.lower()) # output:i will win
print(challenge.upper()) # output:I WILL win

#String concatenation- joining two strings

a="30 days"
b="30 hours"
c= a+b
print(c) # 30 days30 hours
a= 'sri'
b= 'ram'
c= a + " " + b
print(c)# output:sri ram

#casefold() usasge
text="Thirty days Thirty hours"
x=text.casefold()
print(x) #output is thirty days thirty hours
y=text.capitalize()
print(y) #output is Thirty days thirty hours

text1="DON'T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
z=text1.capitalize()
print(z) #output is Don't trouble trouble until trouble troubles you.
w=text1.isalpha()
print(w) #output is False
v=text1.isalnum()
print(v) #output is False

text2='a'
x=text2.isalpha()
print(x) #output is True
num1="1234"
y=num1.isalnum()
print(y) #output is True
num2="1234abcd"
z=num2.isalpha()
v=num2.isalnum()
print(z) #output is False
print(v) #output is True
