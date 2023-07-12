#Function to print multiple chances

def Chance():
    """function to give multiple chances to enter number."""
    while True:
        try:
            num=int(input("Enter a number :"))
            print("typed number is :",num)
            break
        except:
            print("you have enter wrong format")
            continue
            
Chance()