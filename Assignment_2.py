#1 a Finding the length of the input string
input_string="Python is a case sensitive language"
print("The length of the input string is: ",len(input_string))

#1 b Reversing the order of the string
input_string="Python is a case sensitive language"[::-1]
print("The reversed string is: ",input_string)

#1 c Using slice function to store "a case sensitive" in new string
input_string="Python is a case sensitive language"
print("The new string formed is: ",input_string[10:26])

#1 d Replacing "a case sensitive" with "object oriented"
print("The string formed post replacing is: ",input_string.replace("a case sensitive","object oriented"))

#1 e Finding index of substring "a" in the input string
print('The index of substring "a" is: ',input_string.find("a"))

#1 f Removing the white spaces from the input string
print("The string formed on removing white spaces is: ",input_string.strip())

#2 Using string formatting to print the output
name=input("Enter your name: ")
SID=int(input("Enter your SID: "))
department_name=input("Enter your department name: ")
CGPA=float(input("Enter your CGPA: "))
intro="Hey, {} Here!\nMy SID is {}\nI am from {} department and my CGPA is {}"
print(intro.format(name,SID,department_name,CGPA))

#3 Using bitwise operators for the following
a=56
b=10
print("a&b = ",a&b) #part a
print("a|b = ",a|b) #part b
print("a^b = ",a^b) #part c
print("Left shift both a and b with 2 bits, a becomes %d and b becomes %d "%(a<<2,b<<2)) #part d
print("Right shift a with 2 bits and b with 4 bits, a becomes %d and b becomes %d "%(a>>2,b>>4)) #part e

#4 Finding the greatest number among three numbers
input_num=[]
print("Enter the three numbers you want to compare:")
for i in range(0,3): # iterating till the range
    num = float(input())
    input_num.append(num) # adding the element
input_num.sort()
print("The greatest number is ",input_num[2])

#5 To check if the word "name" is present in the string entered by the user
input_str=input("Enter the string:")
if "name" in input_str:
    print("Yes")
else:
    print("No")

#6 To check if the input lengths can form a triangle
side1=float(input("Enter the first side of the triangle: "))
side2=float(input("Enter the second side of the triangle: "))
side3=float(input("Enter the third side of the triangle: "))
side1=int(side1)
side2=int(side2)
side3=int(side3)
if (side1+side2>side3) & (side1+side3>side2) & (side2+side3>side1):
    print("Yes")
else:
    print("No") 
