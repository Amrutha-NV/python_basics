#Write a program to store seven fruits in a list entered by the user.
basket=[]
for i in range(0,7,+1):
    fruit=input(f"enter the fruit:")
    basket.append(fruit)
print(basket)

#Write a program to accept marks of 6 students and display them in a sorted manner.
marks=[]
for i in range(0,6,+1):
    score=int(input(f"enter the score:"))
    marks.append(score)
marks.sort()
print(marks)

#Write a program to sum a list with 4 numbers
l=[12,23,44,56,21,90]
add=0
for  i in range(len(l)):
    add+=l[i]
print(add)
print(sum(l))

#Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))

#Check that a tuple type cannot be changed in python.
a=(1,2,3,4)
a.append(8) #attribute error