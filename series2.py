#2+5+8+11+.... upto n terms
n=int(input("Enter the value of n terms:"))
i=0
a=2
s=0
while(i<n):
    a=a+3
    s=s+a
    i=i+1
print("The addition of the series is:",s)
    
