n=int(input("Enter max width of the rhombus: "))
for i in range(n):
    print(" "*(n-1-i),end=" ")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
for k in range(n-1):
    print(" "*(k+1),end=" ")
    for l in range(n-k-1):
        print(chr(65+l),end=" ")
    print()
    


#Rhombus