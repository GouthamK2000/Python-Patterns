r=int(input("Enter the no. of rows: "))
c=int(input("Enter the no. of columns: "))
for i in range(r):
    for j in range(c):
        print(chr(97+i),end=" ") #use j inplace of i if you want to increase alphabets colunwise
    print()

#chr(65)--A
#chr(97)--a