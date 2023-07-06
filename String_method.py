s = "hello welcome to my page."
str_1 ="hii"
join = ['hello', 'welcome', 'to', 'my', 'page.']
spacestr = "    abcdefg     "
try:
    class string:
        """This function contain all the list functions."""
        def __init__(self,str):
             self.str=str
        def Strlength(self):
            """Function Return the length of the string."""
            print("length of the string :",len(self.str)) 
        def StrType(self):
            """Function To find the Type."""
            print("Type of the string :",type(self.str))
        def StrSclic(self):
            """Sclicing function"""
            print("String between index :",self.str[6:14])
            print("reverse of word welcome :",self.str[-13:-20:-1])
            print("complete string :",self.str[::])
            print("reverse string :",self.str[::-1])
        def StrAddMUlti(self,str1,intstr:int):
            """function to add two string"""
            print("addition of string :",self.str + str1)
            """function to copy string multiple time"""
            print("multiplication string :",self.str * intstr)   
        def StrMembership(self):
            """Membership function"""
            print("Membership operator in string  :","to" in self.str)
        def StrFind(self,word:str):
            """finf function"""
            print("find ",word, "in the string or not ?(-1):",self.str.find(word))
        def StrCount(self,countStr:str):
            """count function"""
            print("counting occurance of the variable :",self.str.count(countStr))
        def StrSplitJoin(self,splitStrr):
            """split and join function"""
            print("spliting the string :",self.str.split(" "))
            print("joining the given string :","".join(splitStrr))
        def StrReplace(self,oldword:str,replace:str):
            """replacefunction"""
            print("Replace the  word :",self.str.replace(oldword,replace))
        def StrRemovigSpace(self,newStr):
            """rstrip, lstrip, strip, function."""
            print("remove space from right :",newStr.rstrip())
            print("remove space from left :",newStr.lstrip())
            print("remove space  :",newStr.strip())
        def StrChangeCase(self):
            """function to change the type of the string."""
            print("uppercase string :",self.str.upper())
            print("lowercase string :",self.str.lower())
            print("capitalize string :",self.str.capitalize())
            print("tittlecase string :",self.str.title())
        def Strtocheck(self):
            """function to check the string"""
            print("Upercase or not :",self.str.isupper())
            print("lowercase or not :",self.str.islower())
            print("isalpha or not :",self.str.isalpha())
            print("isalnum or not :",self.str.isalnum())
            print("istittle or not :",self.str.istitle())
            print("isnumeric or not :",self.str.isnumeric())
            print("isspace or not :",self.str.isspace())
        def StrWordBetwn(self,wordbetn,lenStr:int,word:str):
            """ This function keep the letter in the center with 10 len and remaining space fill with * symbol"""
            print(wordbetn.center(lenStr,word))
    ob=string(s)
    ob.Strlength()
    ob.StrType()
    ob.StrSclic()
    ob.StrAddMUlti(str_1,2)
    ob.StrMembership()
    ob.StrFind("to")
    ob.StrCount("to")
    ob.StrSplitJoin(join)
    ob.StrReplace("hello","hey")
    ob.StrRemovigSpace(spacestr)
    ob.StrChangeCase()
    ob.Strtocheck()
    ob.StrWordBetwn(str_1,10,"*")
except Exception as e:
    print(e)
