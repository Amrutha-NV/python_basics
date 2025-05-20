#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
hindi_to_english={
    "panni":"water",
    "ped":"tree",
    "kaana":"food"
}
word=input("enter the word you want to know the meaning of:")
print(hindi_to_english[word]) # returns key value pairs in the form of tuple

#Write a program to input eight numbers from the user and display all the unique numbers (once).
numbers=set() #create an empty set
for i in range (8):
    num=int(input("enter the number:"))
    numbers.add(num)
print(numbers)

#What will be the length of following set s: s = set() s.add(20) s.add(20.0) s.add('20') # length of s after these operations?
s=set()
s.add(20)
s.add(20.3)
s.add('20')
print(len(s)) #answer is 2 

#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
my_dict={}
for i in range (4):
    key=input("enter your name:")
    value=input("enter your fav language:")
    my_dict[key]=value
print(my_dict)

#If the names of 2 friends are same; what will happen to the program in problem
#ans: whenever the same name is encountered again the vlaue of the key will be overwritten
#If languages of two friends are same; what will happen to the program in problem
#nothing will be overwritten values of value in the key value pair can be same

#Can you change the values inside a list which is contained in set S? s = {8, 7, 12, "Harry", [1,2]}
s = {8, 7, 12, "Harry", [1,2]}
#error unhashable type list we cannot add a list to a set
