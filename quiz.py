question=input("are you ready for quiz ?(Y/N):")
score=0

try:
    a1=input("1.Pytho is dynamic or static language?:")
    if a1.lower() == "dynamic":
        score+=1
        print("correct answer")
    else:
        print("wrong answer")
    
    a2=input("2.Python is high level or low level language?:")
    if a2.lower() == "high level" or a2.lower() == "high" :
        score+=1
        print("correct answer")
    else:
        print("wrong answer")
    
    a3=input("3.Who devlope Python language? :")
    if a3.lower() == "guido van rossam":
        score+=1
        print("correct answer")
    else:
        print("wrong answer")

    a4=input("4.how to check the data type of variable? :")
    if a4 == "type()" :
        score+=1
        print("correct answer")
    else:
        print("wrong answer")

    a5=input("5.how to check the length of the variable? :")
    if a5 == "len()":
        score+=1
        print("correct answer")
    else:
        print("wrong answer")

    print("your score :",score/5*100)
except Exception as e:
    print(e)
      