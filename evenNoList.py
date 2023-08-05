#program to generate the list of only even no from the given list.

l=[1,2,3,4,5,6,7]
l1=[]

def ev(num,apL):
    """ This function check even no and save it in another list ."""    
    for i in num:
        if i%2==0:
            apL.append(i)
        else:
            continue
    print("List :",num)
    print("appended even list is :",apL)
ev(l,l1)


    