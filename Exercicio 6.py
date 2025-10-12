def calculus():
    num1 = int(input())
    operation= input("fun.(+,-,*,/,Clear,Exit): ")
    while operation not in ("+","-","/","*","Clear","Exit"):
        print("insert another function")
        operation= input("fun.(+,-,*,/,Clear,Exit): ")
    if operation == ("Clear"):
        return
    elif operation == ("Exit"):
        offbutton == True
    num2 = int(input())
    if operation == ("+"): res=num1+num2
    elif operation == ("-"): res=num1-num2
    elif operation == ("/"): res=num1/num2
    elif operation == ("*"): res=num1*num2
    print ("res: ",res)
offbutton=False
print ("\tCalculadora")
while offbutton == False:
    calculus()