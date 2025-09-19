num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))
num4=int(input("Enter a number: "))

if num1>num2 and num1>num3 and num1>num4:
    print("number 1 is greter than all numbers")
elif num2>num3 and num2>num4 and num2>num1:
    print("number 2 is greter than all numbers")
elif num3>num4 and num3>num1 and num3>num2:
    print("number 3 is greter than all numbers")
elif num4>num1 and num4>num2 and num4>num3:
    print("number 4 is greter than all numbers")

