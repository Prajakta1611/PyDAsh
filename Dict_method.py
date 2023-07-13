d={"name":"prajakta","class":"tycs","roll-no":8}
class Dict:
    """THIS CLASS CONTAIN ALL THE DICT FUNCTION."""
    def __init__(self,dict:dict):
        self.dict = dict
    def DictType(self):
        """THIS FUNCTION PRINT THE TYPE OF DICT."""
        print("type:",type(self.dict))
    def DictLen(self):
        """THIS FUNCTION PRINT THE LEN OF THE DICT."""
        print("len :",len(self.dict))
    def DictKey(self):
        """THIS FUNCTION PRINT THE KEYS FROM THE DICT."""
        print("keys in list :",self.dict.keys())
    def DictValue(self):
        """THIS FUNCTION PRINT THE VALUE FROM THE DICT."""
        print("values in list:",self.dict.values())
    def DictItems(self):
        """THIS FUNCTION PRINT THE ITEMS FROM THE DICT."""
        print("items in list:",self.dict.items())
    def DictShowVal(self,val):
        """ THIS FUNCTION PRINT THE VALUE """
        print("value",val,":",self.dict[val])
    def DictPop(self,a):
        """THIS FUNCTION DELETE THE VALUE FROM THE DICT."""
        print("Removed item:",self.dict.pop(a))
        print("after:",self.dict)
        print("Removed item :",self.dict.popitem())
        print("after removing :",self.dict)
o=Dict(d)
o.DictType()
o.DictLen()
o.DictKey()
o.DictValue()
o.DictItems()
o.DictShowVal("name")
o.DictPop("class")