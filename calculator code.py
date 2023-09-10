a=int(input("Enter any number : "))
b=int(input("Enter any number : "))
print("Enter 1 for Subtraction    2 for Addition    3 for Multiply    4 for Division")
ch=int(input("Enter choice : "))
if(ch==1):
    print("Difference of ",a,"-",b,"=",a-b)
elif(ch==2):
    print("Sum of ",a,"+",b,"=",a+b)
elif(ch==3):
    print("Product of ",a,"*",b,"=",a*b)
elif(ch==4):
    print("Division of ",a,"/",b,"=",a/b)
else:
    print("Wrong choice")
