h=int(input("Enter the height: "))
for i in range(h):
   print(" "*(h-1-i)+(str(i+1)+" ")*(i+1))

#Another using nested for loop

# n=int(input("Enter the height of the pyramid: "))
# for i in range(n):
#     print(" "*(n-i-1),end=" ")
#     for j in range(i+1):
#         print("#",end=" ")
#     print()