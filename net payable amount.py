pa=int(input("Enter the Purchase amount: "))
if(pa>5000):
       npa=pa-(pa*0.1);
else:
    npa=pa;
print("Net payable amount is: ",npa);
