import re

sentence="Welcome to Luminar"
x=re.search("to",sentence)
print(x)

#if no matches found ,the value None is returned

y=re.search("\s",sentence)
print(y)