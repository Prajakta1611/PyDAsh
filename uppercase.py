#PYTHON PROGRAM TO PRINT THE LIST OF UPPERCASE LETTER PRESENT IN A GIVEN STRING.

str="heLLow WELcome to my proJect."
upper=[]
for i in str:
    if i.isupper() == True:
        upper.append(i)
print(upper)


