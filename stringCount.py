d={"name":"ojas","age":11,"skills":["java","python","c"],"tech":"english","spoke":"hindi"}

#To COUNT HOW MANY STRING ARE THERE
count=0
for i in d:
    if type(d[i])==str:
        count+=1
    elif type(d[i])==list:
        for j in d[i]:
            if type(j)==str:
                count+=1
print(count)