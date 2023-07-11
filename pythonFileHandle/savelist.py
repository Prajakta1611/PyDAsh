l=[1,2,4.3,5,8]
try:
    f=open("list.txt",'w')
    f.write(str(l))
    f.close()
except Exception as e:
    print(e)