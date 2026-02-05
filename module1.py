user=input("enter the elment: ")
my_list=user.split()

print("original list: ",my_list)

if len(my_list)>1:
    my_list[0],my_list[-1]=my_list[-1],my_list[0]

print("After intecange first and last: ",my_list)