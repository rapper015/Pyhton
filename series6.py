#1+2+4+7+11+.... upto n terms
n=int(input("Enter the number of terms:"))
i=1
a=1
s=1
while(i<n):
    a=a+1
    s=s+a
    a=a+i
    i=i+1
print("The sum of the series is:",s)
