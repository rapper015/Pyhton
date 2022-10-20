n=float(input("Enter the number of telephone call: "))
if(n<=75):
    c=250.0;
elif(n<=150):
    c=250+((n-75)*0.80);
elif(n<=225):
    c=250+(75*0.80)+((n-150)*1);
else:
    c=250+(75*0.80)+(75*1)+((n-225)*1.20);
print("Telephone bill is: ",c);
