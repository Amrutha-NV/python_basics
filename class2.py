#variable: a given to the memory location storing the data
# keywords/identifierss: reserved words in python cannot be used as a variable
#taking input
a=input("enter the input:")
#taking integer type input
b=int(input("enter the input:"))
#taking floating type input
c=float(input("enter the input:"))

#type() function
#is used to determine the type of a variable
print(type(a)) #output is a string
print(type(b)) #output is an integer
#type casting
#converting one type of variable to other
print(str(a))
print(int(c))
print(float(b))

#write a python program to add two numbers
a=int(input("enter the number 1:"))
b=int(input("enter the number 2:"))
sum=a+b
print(sum)

#wap to find the denominator when a number is divided by y
x=int(input("enter the numerator"))
y=int(input("enter the denominator"))
z=x%y
print(f"the remainder is{z}")

#wap to find the avg of two numbers
a=int(input("enter the number 1:"))
b=int(input("enter the number 2:"))
avg=(a+b)/2
print(avg)

#wap to find the square of the give number
a=int(input("enter the number :"))
square=a**2
print(square)