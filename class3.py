#Write a python program to display a user entered name followed by Good Afternoon using input () function.
a=input("enter your name:")
b="Good Afternoon"
print(a+" "+b)

#Write a program to fill in a letter template given below with name and date.
#letter = ''' Dear <|Name|>, You are selected! <|Date|> '''
name=input("enter your name:")
date=input("enter today's date in the format dd/mm/yy:")
letter=print(f" Dear {name}, You are selected! \n {date}")
print("letter")

#Write a program to detect double space in a string.Replace the double space from problem 3 with single spaces.
string_variable="hi  amrutha how are you doing"
string_variable.find("  ")
string_variable.replace("  "," ")

#Write a program to format the following letter using escape sequence characters. 
#letter = "Dear Harry, this python course is nice. Thanks!"
letter = "Dear Harry,\n this python course is nice.\n Thanks!"
print(letter)
