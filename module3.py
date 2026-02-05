user=input("Enter elements of the list: ")
list=user.split()

count=0

for _ in list:
    count+=1

print("Length of the list is: ",count)