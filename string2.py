#to print vowels in string and save them in list.
try:
    s="hellow my name is prajakta"
    s1=[]
    for i in s:
        if i in "aeious":
            s1.append(i)
    print(s1)
except Exception as e:
    print(e)