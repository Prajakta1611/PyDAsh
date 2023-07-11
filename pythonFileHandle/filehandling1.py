# Python program to create a file and writea file.
try:
    f=open("abc.txt",'w+')
    f.write("hello welcome\n")
    f.write("its my python project")
    print(f.read())
    f.close()
except Exception as e:
    print(e)