#this file contain all the list method.

l=[2,10,26,5,8,3,"4","hello",5.6,"python"]
l2=[2,1]
extend_list=[3,22]

try:
    class List:
        """This function contain all the list functions."""
        def __init__(self,list:list):
            self.list=list
        def Listlen(self):
            """function to find length."""
            print("len of list :",len(self.list))
        def ListTyp(self):
            """Function to check type."""
            print("Type of list :",type(self.list))
        def ListOfIntVal(self,list2:list):
            """append function."""
            self.list2=list2
            for i in self.list:
                if type(i) == int or type(i) == float:
                    self.list2.append(i)
            print("new list is :",self.list2)
        def ListExtend(self):
            """Extendfunction"""
            self.list.extend(self.list2)
            print("extended list :",self.list) 
        def ListSort(self):
            """sort function"""
            self.list2.sort()
            print("sorted list is :",self.list2)
            self.list2.sort(reverse=True)
            print("sorted list is :",self.list2)
        def listMinMax(self):
            """Min max function"""
            print("max value of new list :",max(self.list2))   
            print("min value of new list :",min(self.list2)) 
        def listInsertVal(self,index:int,value:int):
            """insert function"""
            self.list2.insert(index,value)
            print("inserted value :",self.list2)
        def ListIndex(self,index:int):
            """Indexfunction"""
            print("index of ",index," is :",self.list2.index(index))
        def ListRemove(self,value:int):
            """remove function"""
            print("delete ",value,"value :",self.list2.remove(value))
            print("after deliting ",value,"value :",self.list2)
        def ListPop(self):
            """pop function"""
            print("remov last value :",self.list2.pop())
            print("after removing last value :",self.list2)
    ob=List(l)
    ob.Listlen()
    ob.ListTyp()
    ob.ListOfIntVal(l2)
    ob.ListExtend()
    ob.ListSort()
    ob.listMinMax()
    ob.listInsertVal(9,99)
    ob.ListIndex(99)
    ob.ListRemove(2)
    ob.ListPop()
except Exception as e:
    print(e)