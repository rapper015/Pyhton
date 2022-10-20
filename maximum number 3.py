n1=input("Enter the first number: ")
n2=input("Enter the second number: ")
n3=input("Enter the third number: ")
if(n1>n2)and(n1>n3):
    max=n1;
elif(n2>n1)and(n2>n3):
    max=n2;
else:
    max=n3;
print("Maximum number is: ",max);
