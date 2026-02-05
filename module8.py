user=input("Enter elements for the tuple : ")
t_ele=tuple(map(int,user.split()))

sum_of_ele=sum(t_ele)

print("The sum of the tuple elements is : ",sum_of_ele)