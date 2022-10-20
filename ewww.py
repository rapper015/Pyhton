name=input("Enter your name:")
print_A=[[" " for i in range(5)]for j in range (5)]
print_B=[[" " for i in range(5)]for j in range (5)]
print_C=[[" " for i in range(5)]for j in range (5)]
print_D=[[" " for i in range(5)]for j in range (5)]
print_E=[[" " for i in range(5)]for j in range (5)]
print_F=[[" " for i in range(5)]for j in range (5)]
print_G=[[" " for i in range(5)]for j in range (5)]
print_H=[[" " for i in range(5)]for j in range (5)]
print_I=[[" " for i in range(5)]for j in range (5)]
print_J=[[" " for i in range(5)]for j in range (5)]
print_K=[[" " for i in range(5)]for j in range (5)]
print_L=[[" " for i in range(5)]for j in range (5)]
print_M=[[" " for i in range(5)]for j in range (5)]
print_N=[[" " for i in range(5)]for j in range (5)]
print_O=[[" " for i in range(5)]for j in range (5)]
print_P=[[" " for i in range(5)]for j in range (5)]
print_Q=[[" " for i in range(5)]for j in range (5)]
print_R=[[" " for i in range(5)]for j in range (5)]
print_S=[[" " for i in range(5)]for j in range (5)]
print_T=[[" " for i in range(5)]for j in range (5)]
print_U=[[" " for i in range(5)]for j in range (5)]
print_V=[[" " for i in range(5)]for j in range (5)]
print_W=[[" " for i in range(5)]for j in range (5)]
print_X=[[" " for i in range(5)]for j in range (5)]
print_Y=[[" " for i in range(5)]for j in range (5)]
print_Z=[[" " for i in range(5)]for j in range (5)]
print_space=[[" " for i in range(5)]for j in range (5)]
#CODE FOR A
def A():
    for row in range(5):
        for col in range (5):
            if ((col==0 or col==4) and row!=0) or ((row==0 or row==2)and (col>0 and col<4)):
                print_A[row][col]="*"
    return print_A
#CODE FOR B
def B():  
    for row in range(5):
        for col in range (5):
            if col==0 or ((row==0 or row==2 or row==4) and (col>0 and col<4)) or (col==4 and row==1) or (col==4 and row==3):
                print_B[row][col]="*"
    return print_B
#CODE FOR C
def C():  
    for row in range(5):
        for col in range (5):
            if ((col==0)and (row!=0 and row!=4)) or ((row==0 or row==4) and col>0):
                print_C[row][col]="*"
    return print_C
#CODE FOR D
def D():  
    for row in range(5):
        for col in range (5):
            if col==0 or (col==4 and (row!=0 and row!=4)) or ((row==0 or row==4) and (col>0 and col<4)):
                print_D[row][col]="*"
    return print_D
#CODE FOR E
def E():  
    for row in range(5):
        for col in range (5):
            if col==0 or ((row==0 or row==2 or row==4) and col>0):
                print_E[row][col]="*"
    return print_E
#CODE FOR F
def F(): 
    for row in range(5):
        for col in range (5):
            if col==0 or ((row==0 or row==2) and col>0):
                print_F[row][col]="*"
    return print_F
#CODE FOR G
def G():  
    for row in range(5):
        for col in range (5):
            if col==0 or (col==4 and (row!=0 and row!=1)) or ((row==0 or row==4) and col>0) or (row==3 and col==2 and col==3):
                print_G[row][col]="*"
    return print_G
#CODE FOR H
def H():  
    for row in range(5):
        for col in range (5):
            if col==0 or col==4 or (row==2 and (col>0 and col<4)):
                print_H[row][col]="*"
    return print_H
#CODE FOR I
def I():  
    for row in range(5):
        for col in range (5):
            if row==0 or row==4 or (col==2 and (row>0 and row<4)):
                print_I[row][col]="*"
    return print_I
#CODE FOR J
def J():  
    for row in range(5):
        for col in range (5):
            if (row==0 or (row==4 and col<3)) or (col==2 and row>0 and row<4):
                print_J[row][col]="*"
    return print_J
#CODE FOR K
def K():  
    for row in range(5):
        for col in range (5):
            if col==0 or (row==0 and col>2) or (row==4 and col>2) or (col==2 and row==1) or (col==2 and row==3):
                print_K[row][col]="*"
    return print_K
#CODE FOR L
def L(): 
    for row in range(5):
        for col in range (5):
            if col==0 or (row==4 and col>0):
                print_L[row][col]="*"
    return print_L
#CODE FOR M
def M():  
    for row in range(5):
        for col in range (5):
            if col==0 or col==4 or ( col==1 and row==1) or (col==2 and row==2) or (col==3 and row==1):
                print_M[row][col]="*"
    return print_M
#CODE FOR N
def N():  
    for row in range(5):
        for col in range (5):
            if col==0 or col==4 or (col==row and col>0 and col<4):
                print_N[row][col]="*"
    return print_N
#CODE FOR O
def O():  
    for row in range(5):
        for col in range (5):
            if ((col==0 or col==4)and (row>0 and row<4)) or ((row==0 or row==4)and (col>0 and col<4)):
                print_O[row][col]="*"
    return print_O
#CODE FOR P
def P():  
    for row in range(5):
        for col in range (5):
            if col==0 or ((row==0 or row==2) and (col>0 and col<4)) or (col==4 and row==1):
                print_P[row][col]="*"
    return print_P
#CODE FOR Q
def Q():  
    for row in range(5):
        for col in range (5):
            if ((col==0 or col==4) and (row>0 and row<3)) or ((row==0 or row==3) and (col>0 and col<4)) or (row==2 and col==2) or (row==4 and col==2):
                print_Q[row][col]="*"
    return print_Q
#CODE FOR R
def R():  
    for row in range(5):
        for col in range (5):
            if col==0 or ((row==0 or row==2) and (col>0 and col<4)) or (col==4 and row==1) or (col==1 and row==3) or (col==2 and row==4):
                print_R[row][col]="*"
    return print_R
#CODE FOR S
def S():  
    for row in range(5):
        for col in range (5):
            if row==0 or row==2 or row==4 or (col==0 and row==1) or (col==4 and row==3):
                print_S[row][col]="*"
    return print_S
#CODE FOR T
def T():  
    for row in range(5):
        for col in range (5):
            if row==0 or (col==2 and row>0):
                print_T[row][col]="*"
    return print_T
#CODE FOR U
def U():  
    for row in range(5):
        for col in range (5):
            if col==0 or col==4 or (row==4 and (col>0 and col<4)):
                print_U[row][col]="*"
    return print_U
#CODE FOR V
def V():  
    for row in range(5):
        for col in range (5):
            if (col==row and col<3) or (col+row==4 and col>2):
                print_V[row][col]="*"
    return print_V
#CODE FOR W
def W():  
    for row in range(5):
        for col in range (5):
            if col==0 or col==4 or (col==1 and row==3) or (col==3 and row==3) or (col==row and row!=1 and col!=1):
                print_W[row][col]="*"
    return print_W
#CODE FOR X
def X():  
    for row in range(5):
        for col in range (5):
            if col==row or (col+row==4 and col!=row):
                print_X[row][col]="*"
    return print_X
#CODE FOR Y
def Y():  
    for row in range(5):
        for col in range (5):
            if (col==row and col<3) or (col+row==4 and col>2) or (col==2 and row>2):
                print_Y[row][col]="*"      
    return print_Y
#CODE FOR Z
def Z(): 
    for row in range(5):
        for col in range (5):
            if row==0 or row==4 or (col+row==4 and (row>0 and row<4)):
                print_Z[row][col]="*"
    return print_Z

                
dict={'A': A ,
      'B': B ,
      'C': C ,
      'D': D ,
      'E': E ,
      'F': F ,
      'G': G ,
      'H': H ,
      'I': I ,
      'J': J ,
      'K': K ,
      'L': L ,
      'M': M ,
      'N': N ,
      'O': O ,
      'P': P ,
      'Q': Q ,
      'R': R ,
      'S': S ,
      'T': T ,
      'U': U ,
      'V': V ,
      'W': W ,
      'X': X ,
      'Y': Y ,
      'Z': Z ,
      }
l=len(name)
for i in range(l):
    c1=name[i]
    for i in range(5):
        for j in range(5):
            print((dict.get(c1)())[i][j],end="")
        print(end="")
        print()    
    print()