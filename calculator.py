
num1=float(input("Enter num1="))
exp=True
while exp:
    op=input("Enter operator")
    num2=float(input("Enter num2="))
    if op=='+':
        res=num1+num2
        print(res)
    elif op=='-':
        res=num1-num2
        print(res)
    elif op=='*':
        res=num1*num2
        print(res)
    elif op=='/':
        res=num1-num2
        print(res)
    elif op=="//":
        res=num1//num2
        print(res)
    elif op=="**":
        res=num1-num2
        print(res)
    else:
        print("INVALID")
    exp=input("Do you want to do more operations? Y/N ")
    num1=res
    if exp.upper()=='N':
        print(f"Final Result=",res)
        exp=False
