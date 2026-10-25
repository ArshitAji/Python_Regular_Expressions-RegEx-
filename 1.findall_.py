import re

sentence="Welcome to luminar technolab..!"
x=re.findall("to",sentence)
print(x)
y=re.findall("hello",sentence)
print(y)