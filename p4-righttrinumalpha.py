user=int(input("Enter the height of  the triangle: "))
for i in range(user):
    for j in range(i+1):
        print(chr(97+j),end=" ")   #Use j+1 for columnwise
    print()


#Use chr(65+i)/chr(65+j) for  capital alphabets. 
#Use  chr(97+i)/chr(97+j) for small alphabets.