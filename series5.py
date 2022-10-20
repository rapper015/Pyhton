# 1+11+111+1111+.... upto n terms
n=int(input("Enter the number of terms:"))
i=1
a=1
s=1
while(i<n):
    a=a*10+1
    s=s+a
    i=i+1
print("The sum of the series is:",s)
