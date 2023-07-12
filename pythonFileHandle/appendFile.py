# FILE HANDLING FUNCTION.

def Appendfile():
    """ TO WRITE A FILE USING APPEND FUNCTION."""
    f=open("abc.txt","a")
    f.write("\n This essay provides an overview of Python language.")
    f.close()
Appendfile()

