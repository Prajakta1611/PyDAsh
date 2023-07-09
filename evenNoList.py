#program to generate the list of only even no from the given list.
l=[1,2,3,4,5,6,7]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        continue

print(l1)

    