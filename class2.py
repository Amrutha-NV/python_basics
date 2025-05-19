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