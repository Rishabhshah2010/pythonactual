def simpleInterest():
    result = (principal * rate * time) / 100
    print("The simple interest is : " , result)
def compoundInterest():
    result2 = principal * (1 + rate/100) ** time - principal
    print("The compound interest is : " , format(result2 , '2f'))
    




principal = int(input("Enter your principal "))
rate = int(input("Enter your rate "))
time = int(input("Enter the number of years "))
interest = input(" Do you want simple interest or compound. Enter s or c(s for simple interest and c for compound interest.)")
if interest == 's':
    simpleInterest()
elif interest == 'c':
    compoundInterest()
else:
    print("Enter one of the specified values")

def simpleInterest():
    result = principal * rate * time
    print("The simple interest is : " , result)
def compoundInterest():
    result2 = principal * rate * time
    print("The compound interest is : " , result2)
