def young():
    print("welcome to young man world.")
    print ("there will be two kinds of young man,ugly and handsome.")
    print("which one you like?")
    look = input("<<<<<<<<")
    if look == "ugly":
        print("nice,you are not a lookist.Aactually,Kris wu will be your boyfriend.")
    elif look == "handsome":
        print("you are asking too much!you have to choose again")
        start()
    else:
        print("you will die alone")
def old():
    print ("hello , unclecon girl")
    print("what age do you like?")

    
    age = int(input(">>>>>>>"))
    if age <= 30:
        young()
    elif age < 55:
            print("yeah,you can marry a old poor man.")
    elif age < 100:    
        print("there are many old rich man waiting for you")
    else:
        print ("maybe the man is died,you can chose again")
        start()

def start():
    print("hello!older woman,do you feel loney?")
    choice = input(">>>>>yes or no>>>>>>")
    if choice == "yes":
        print("there are two type of men,old or young")
        print("which man you want to marry?")
        type = input(">>>>>>>")
        if type == "old":
            old()
        elif type == "young":
            young()
        else:
            print("get out of here")
    else:
        print("get out of here")

start()



