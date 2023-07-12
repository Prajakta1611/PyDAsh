#FILEHANDLING FUNCTION 
try:
    def SeakTell():
        """ TO READ A FILE \n Seek: move the index where we want.\n Tell:tell us the curruent index of the cursur"""
        f=open("abc.txt","r")
        print("Using read :",f.read())
        f.seek(0)
        #readline print the single instance.
        print("\n Using readline :",f.readline())
        f.seek(0)
        #readlines print all the file bt take it as a single list instance.
        print("Using readlines :",f.readlines())
    SeakTell()
except Exception as e:
    print(e)
