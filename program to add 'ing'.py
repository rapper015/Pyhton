sf=""
s=input("Enter the word to change:")
l=len(s)
if(l>=3):
    c=s[l-3:]
    if(c=="ing"):
        sf=s+"ly"
    else:
        sf=s+"ing"
else:
    sf=s
print("New word is:" , sf)
