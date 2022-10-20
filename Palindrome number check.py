n=int(input("Enter the number to check:"))
s=0
a=n
while(a>0):
    r=a%10
    s=(s*10)+r
    a=a//10
if(s==n):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
    
