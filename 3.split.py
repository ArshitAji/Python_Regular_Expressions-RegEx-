import re

sentence="Welcome To Luminar Technolab..!"
x=re.split("\s",sentence)            #split at each match =whitespace
print(x)

y=re.split("To",sentence)
print(y)