w=int(input("Enter the weight of the parcel: "))
if(w<=20):
    c=25;
else:
    c=25;
    w=w-20;
    while(w>0):
        w=w-10;
        c=c+5;
print("Charge is: ",c);
