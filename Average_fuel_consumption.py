def start():
    print("Avarage fuel consumption")
start()
while True:
    answer = str(input("Do you want to use the Hungarian or the United State version?(H/US):  \nType exit if you want to finish the program.: "))
    if answer.lower() in ["hungarian","hungary","h","magyar" ]:
        km = int(input("How manny km you did?: "))
        l = int(input("How manny liter fuel did you used?: "))
        av = round((l*100)/km,2)
        print("Your avarage fuel usage is: " + str(av) + " liter/kilometer")

    elif answer.lower() in ["unitedstate","united state","us","usa","united state of america","american","america","unitedstateofamerica" ]:
        m = int(input("How manny miles you did?: "))
        g = int(input("How manny gallon fuel did you used?: "))
        av = round((1*m)/g,2)
        print("You can travel " + str(av) + " miles with a gallon fuel.")
    elif answer.lower() in ["exit","stop"]:
        break
    else:
        print("Please type H or US ")
        continue

