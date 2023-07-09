#program to check the number is prime or not

try:
    num=int(input("enter a number :"))
    x=0
    def fun(num):
        """This fuction check the enter no is prime or not"""
        for i in range(2,num):
            if num%i==0:
                x = 1
                break
            else:
                x = 0
        if x == 1:
            print("not a prime")
        else:
            print("prime")
    fun(num)
except Exception as e:
    print(e)


