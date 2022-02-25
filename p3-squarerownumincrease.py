row=int(input("Enter the no. of rows: "))
col=int(input("Enter the no. of columns: "))
for i in range(row):
    for j in range(col):
        print((i+1),end=" ")
    print()


""" row=int(input("Enter the no. of rows: "))
col=int(input("Enter the no. of columns: "))
for i in range(row):
    for j in range(col):
        print((j+1),end=" ")               Here j is used in place of i, if we want to print  same elements columnwise
    print()

 """