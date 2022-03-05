n=int(input("Enter n: "))
for i in range(n):
    print(" "*(n-1-i)+" # ",end=" ")
    if i>1:
        print(" "*(2*(i-1))+"#",end=" ")
    print()