#first N terms of the fibonacci series.
n=int(input("Enter the n terms: "))
a=0;
b=1;
i=1;
print(a,b);
while(i<=n):
    c=a+b;
    print(c);
    a=b;
    b=c;
    i=i+1;
