import re
sentence="Welcome to luminar"
x=re.sub("\s","_",sentence)
print(x)

#replaces every whitespae with underscore
#the sub() function replaces the matches with the text of your choice