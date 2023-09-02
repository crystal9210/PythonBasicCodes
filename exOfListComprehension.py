#ex of List Comprehension
#the general syntax of a list comprehension is as follows:
# new_list = [expression for item in iterable if condition]

#ex1
squares=[x**2 for x in range(10)]
print(squares)

#ex2
lam=list(map(lambda x:x**2,range(10)))
print(lam)


