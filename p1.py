#printing n no of elemtns in one single row

sym=input("Enter the  symbol you want: ")
num=int(input("Enter the no. of elements you want: "))
for i in range(num):
    print(sym+" ",end="")  #,end=" " allows us to preventing the cursor from moving to the next line
