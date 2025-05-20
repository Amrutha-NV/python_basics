'''#Write a program to print multiplication table of a given number using for loop/while loop.
number=int(input("enter the number:"))
i=0
for i in range(1,11,+1):
    print(f"{number}*{i}={number*i}")
    
number=int(input("enter the number:"))
i=0
while(i<=10):
    print(f"{number}*{i}={number*i}")
    i+=1


#Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
for item in l:
    if item.startswith("S"):
        print(f"Good Morning {item}")
        
#Write a program to find whether a given number is prime or not.
number=int(input("enter a number:"))
is_prime=True
for i in range(2,int(number**.5),+1):
    number%i==0
    is_prime=False
    break
if(number<=1):
    print(False)
elif(is_prime==True):
    print(f"the given number {number} is prime")
elif(is_prime==False):
    print(f"the given number {number} is  not prime")
else:
    print("enter a proper number")'''

#Write a program to find the sum of first n natural numbers using while loop.
n=int(input("enter the nubers until which you want to find the sum:"))
i=0
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)

#Write a program to calculate the factorial of a given number using for loop.
n=int(input("enter the nubers until which you want to find the factorial:"))
i=1
fact=1
while(i<=n):
    fact*=i
    i+=1
print(fact)

#Write a program to print the following star pattern.
'''
*
***
***** for n = 3'''
n=int(input("enter the value to print pattern"))
i=1
for i in  range(1,n+1,+1):
    print("*"*(2*i-1))


#Write a program to print the following star pattern:
'''
*
**
*** for n = 3'''
n=int(input("enter the value to print pattern"))
i=1
for i in  range(1,n+1,+1):
    print("*"*i)

'''Write a program to print the following star pattern.
* * *
*   * for n = 3
* * *'''
n=int(input("enter the value to print pattern"))
i=1
for i in  range(1,n+1,+1):
    if(i==1 or i==n):
         print("*"*n)
    else:
       print("*"+" "*(n-2)+"*") 
        
        
        
#Write a program to print multiplication table of n using for loops in reversed order.
number=int(input("enter the number:"))
i=10
for i in range(10,0,-1):
    print(f"{number}*{i}={number*i}")