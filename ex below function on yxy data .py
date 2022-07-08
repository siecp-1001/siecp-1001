from dataclasses import replace
import re
c="I.like. this book"
c1= re.sub(r'[^\w\s]','',c)
print(c1)





import string
s="I.like. this book"
for c in string.punctuation:
    s= s.replace(c,"") 
    print(s)