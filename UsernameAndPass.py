print("welcome to my web")
#this a and b are saved value in databases which already converted to lower case.
a="abc123"
b=231
username=input("enter a name:")
username=username.lower()
password=int(input("enter a password:"))
if username == a and password == b:
    print("login successful")
else:
    print("username/password is inncorrect")