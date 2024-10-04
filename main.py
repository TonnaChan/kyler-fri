def visitorCheck(name):
    if name == "Alfred":
        print("Welcome home!")
    elif name == "John" or name == "Peter":
        print("Get out of here, " + name + "!")
    elif name == "Desiree":
        print("I've been thinking about you, " + name)
    elif name == "Kyler":
        print("Hello " + name + "!")
    else:
        print("Go away or I will call the police!")

def addNumbers(num1, num2):
    ans = num1 + num2
    print(ans)

def multiplyNumbers(num1, num2):
    ans = num1 * num2
    print(ans)

multiplyNumbers(12, 9)