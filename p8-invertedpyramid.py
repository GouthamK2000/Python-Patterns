h=int(input("Enter the pyramid height: "))
for i in range(h):
    print(" "*i,end=" ")
    for j in range(h-i):
        print(chr(97+i),end=" ")
    print()

#print i+1, j+1 for increasing nums from colwise and rowwise.