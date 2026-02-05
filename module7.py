user=input("Enter the elements of the tuple: ")

ele=user.split()
ele=tuple(map(int,ele))

k=int(input("Enter the value of K(index of tuple): "))

t_sort=sorted(ele)
print("The size of the tuple is: ",len(t_sort))

min_k_elements=t_sort[:k]
max_k_elements=t_sort[-k:]

print("The minimum K element are: ",min_k_elements)
print("The maxminum K elements are : ",max_k_elements)
