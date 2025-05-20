#Write a program to find out whether a given post is talking about “Harry” or not.
post=input("enter your post:")
if("Harry" in post):
    print("the post is taking about harry")
else:
    print("the post is not talking about harry")
    
#Write a program to find the greatest of four numbers entered by the user.
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=int(input("enter the number"))
if a>b and a>c and a>d:
    print(f"{a} is a greater number")
elif b>a and b>c and b>d:
    print(f"{b} is a greater number")
elif c>a and c>b and c>d:
    print(f"{c} is a greater number")
elif d>a and d>b and d>c:
    print(f"{c} is a greater number")
else:
    print("all the numbers are equal")
    
#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
marks1=int(input("enter the marks"))
marks2=int(input("enter the marks"))
marks3=int(input("enter the marks"))
total_percentage=((marks1+marks2+marks3)/300)*100
if (marks1>=33 and marks2>=33 and marks3>=33 and total_percentage>=40):
    print(f"the student has passed the subjects with{total_percentage}")
else:
    print(f"student has failed the subjects with {total_percentage}")
    
#A spam comment is defined as a text containing following keywords:
#“make a lot of money”, “buy now”, “buy now”, “click this”. Write a program to detect these spams.
comment=input("enter your comment:")
if "make a lot of money"in comment or "buy now"in comment or "subscribe this"in comment or "click this" in comment:
    print("this is a spam comment")
else:
    print("this is not spam comment")
    
#Write a program to find whether a given username contains less than 10 characters or not.
username=input("enter the username:")
if(len(username)==10):
    print("the username contains 10 characters")
elif(len(username)>10):
     print("the username contains more than 10 characters")
else:
     print("the username contains less than 10 characters")

#Write a program which finds out whether a given name is present in a list or not.
name_list=["anu","anup","arnav","arya"]
name=input("enter the name:")
if(name in name_list):
    print("name found")
else:
    print("name not found")

'''Write a program to calculate the grade of a student from his marks from the following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F'''
marks=int(input("enter the marks of the student:"))
if(marks>90 and marks<=100):
    print("Grade-Ex")
elif(marks>80 and marks<=90):
    print("Grade-A")
elif(marks>70 and marks<=80):
    print("Grade-B")
elif(marks>60 and marks<=70):
    print("Grade-C")
elif(marks>50 and marks<=60):
    print("Grade-D")
elif(marks<50):
    print("Grade-D")
else:
    print("Enter proper marks")

