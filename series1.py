#2+5+8+11+.... upto n
n=int(input("Enter the value of n:"))
i=1
s=0
while(i<=n):
    i=i+3
    s=s+i
print("The addition of the series is:",s)
