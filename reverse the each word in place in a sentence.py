sen=input("Enter the sentence to reverse each word:")+" "
sf=""
wf=""
for i in range (len(sen)):
    c=sen[i]
    if(c==" "):
        sf=sf+wf+" "
        wf=""
    else:
        wf=c+wf
print("The final sentence with each word reversed is:",sf)
        

        
