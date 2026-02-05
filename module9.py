rows=int(input("Enter the number of rows in the matrix: "))

matrix=[]

for i in range(rows):
    user=input("Enter elements of row: ")
    row=tuple(map(int,user.split()))
    matrix.append(row)

sum_of_row=[sum(row) for row in matrix]

print("Row-wise sums of the tuple matrix are: ",sum_of_row)
