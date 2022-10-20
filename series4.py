#Display series 2, 5, 8, 11, .... upto n terms
n=int(input("Enter the value of n:"))
i=2
a=1
while(a<=n):
    print(i,end=", ")
    i=i+3
    a=a+1
