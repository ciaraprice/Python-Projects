#keep a history of calculations your calculator does - what structure?
#add another menu option - see history


hisDict ={}
counter = 1

isOn = True
print("Welcome to Ciara's Calculator")


while isOn:
    num = input("Enter a list of numbers: ")
    numList = num.split()
    numList = list(map(float, numList))
    print(numList)


    operator = input("Enter an operator( * , /, + or  -) to apply to your numbers: ")
    total = 0.0


    for number in range(len(numList)):
        if number == 0:
            total = numList[number]
        else:
            if operator == "*":
                total = total * numList[number]
            elif operator == "+":
                total = total + numList[number]
            elif operator == "-":
                total = total - numList[number]
            elif operator == "/":
                total = total / numList[number]
    print(total)

    inputDict = {
        "operator": operator,
        "number list": numList,
        "total": total
    }

    hisDict[counter] = inputDict

    viewHis = input("See your history? Type Y for yes or N for no: ")
    if viewHis == "Y" or "y":
        for x in hisDict:
            print(str(x) + ". ", end="")
            s = len(hisDict[x]["number list"])
            nums = hisDict[x]["number list"]
            for i in range(0, s):  # check the length of the hisDict number list
                print(str(nums[i]) + " ", end="")
                if i != s - 1:
                    print(hisDict[x]["operator"], "", end="")
            print("=", hisDict[x]["total"])


    continueCal = input("Do you want to continue? Type N or n to exit. Otherwise press enter: ")
    if continueCal == "N" or continueCal == "n":
        isOn = False
        print("This is your history: ", hisDict)
        print("goodbye")

    #historyDict counter
    counter = counter + 1