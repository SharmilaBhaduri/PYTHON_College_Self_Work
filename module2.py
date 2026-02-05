user=input("Enter the element of the list : ")
my_list=user.split()

print("Original list: ",my_list)

e1=int(input("Enter the index of the 1st element for swap: "))
e2=int(input("Enter the index of the 2nd eement for swap: "))

if e1>=len(my_list) or e2>=len(my_list) or e1<0 or e2<0:
    print("sorry no position is declare")

else:
    my_list[e1],my_list[e2]=my_list[e2],my_list[e1]

    print("After swapping : ",my_list)
    