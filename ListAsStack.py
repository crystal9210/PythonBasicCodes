#In Python, it's possible to store elements of different types in a list. Since Python is a dynamically-typed language, different types of objects can coexist freely within a list. However, when trying operations that depend on type, such as summing all the elements or sorting them, there's a potential for errors to occur.
stack=[3,4,5]
stack.append('apple') #
# stack.append()
print(stack)

#treat all elements inside a list as strings and concatenate them
# (concatenate：物事を一連の順序で結合または結合することを意味)

result=''.join(map(str,stack))
print(result)

print(stack.pop())
print(stack)

#ex2;specify a function using a lambda expression as the first argument of the 'map' function

numbers=[1,2,3,4,5]
doubled_numbers=list(map(lambda x:x*2,numbers))
print(doubled_numbers)


