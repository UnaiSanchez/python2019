
for i in range(10):
    for j in range(i):
        print("-",end=" ")
    print("X",end=" ")
    for j in range(9-i):
        print("-",end=" ")     
    print()
print()
for i in range(10):
    if i < 5:
        for j in range(i):
            print("-",end=" ")
        print("X",end=" ")
        for j in range(8-2*i):
            print("-",end=" ")
        print("X",end=" ") 
        for j in range(i):
            print("-",end=" ")
        print()
    else:
        for j in range(9-i):
            print("-",end=" ")
        print("X",end=" ")
        for j in range(2*i-10):
            print("-",end=" ")
        print("X",end=" ") 
        for j in range(9-i):
            print("-",end=" ")  
        print()  