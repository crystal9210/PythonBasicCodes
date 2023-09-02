#a test nested List Conprehension code

#the general syntax of a nested list comprehension is as following
#new_list=[[expression for inner_item in inner_iterable] for item in outer_iterable]

#generate a nested list
#add:[expression for item in iterable]
matrix1 = [[j for j in range(5)] for i in range(3)]

print(matrix1)


matrix2 = [[j**2 for j in range(5)] for i in range(3)]

print(matrix2)

#ex2:create a 1-dimenyonal list from a 2-dimensyonal matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#'num' and 'row' variable's scope is in the flattened = [num for row in matrix for num in row] sentence.
flattened = [num for row in matrix for num in row]
#flattened = []
#for row in matrix:
#    for num in row:
#        flattened.append(num)


print(flattened)

#ex3:nested comprehension with conditions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = [num for row in matrix if sum(row) > 10 for num in row if num % 2 == 0]
#evens=[]
#for row in matrix:
# if sum(row)>10: →サブリストの要素の合計が10を越える場合のみ、そのサブリストを処理対象とする
#   for num in row:
#     if num%2==0:
#       evens.append(num)
print(evens)

