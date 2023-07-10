#PYTHON PROGRAM TO PRINT THE LIST OF UPPERCASE LETTER PRESENT IN A GIVEN STRING.

str="hellow WELcome to my project."
l=[]
for i in str:
    if i.isupper():
        l.append(i)
    elif i.islower():
        a=i.upper()
        l.append(a)
print(l)


