#This file contain all the tuple function.

t=(2,10,26,5,8,3,8,8,8,"4","hello",5.6,"python")
t1=(1)
t2=(1,2,6,4,32,34,1,2,3,44,55)

class tuple:
    """"THIS CLASS CONTAIN EVERYTHING ABOUT TUPLE"""
    def __init__(self,tuple:tuple):
        self.tuple=tuple
    def TuplePrintT(self):
        """FUNCTION TO PRINT THE GIVEN TUPLE"""
        print(self.tuple)
    def TupleType(self,tup:tuple):
        """"FUNCTION TO FIND THE TYPE """
        print("type of tuple :",type(tup))
        print("type of tuple :",type(self.tuple))
    def Tuplelen(self):
        """"FUNCTION TO PRINT THE LEN """
        print("len of the given tuple :",len(self.tuple))
    def TupleValue(self):
        """"FUNCTION TO EXTRACT THE VALUE """
        print("extract the tuple from [0:5] :", self.tuple[0:5])
        print("extract the tuple from [6] : ",self.tuple[6])
    def TupleCount(self,a:int):
        """"FUNCTION TO COUNT THE OCCURANCE OF THE VALUE """
        print("count of ",a,"is :",self.tuple.count(a))
    def TupleMaxMin(self,tuplem:tuple):
        """"FUNCTION TO FIND THE MAX MIN VALUE """
        print("max is :",max(tuplem))
        print("min is :",min(tuplem))
ob=tuple(t)
ob.TuplePrintT()
ob.TupleType(t1)
ob.Tuplelen()
ob.TupleValue()
ob.TupleCount(8)
ob.TupleMaxMin(t2)