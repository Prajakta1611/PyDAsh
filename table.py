#program to pint table .

num=int(input("Enter a number :"))

def table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
table(num)

