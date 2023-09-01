fruits=['orange','apple','pear','banana','orange','orange','banana']

print(fruits)
print(fruits.count('orange')) #the output number is the number of 'orange' in the list of fruits
print(fruits.count('pear'))

print(fruits.index('orange')) #the output number is the index of the first 'orange' element in the list.
print(fruits.index('pear'))

fruits.reverse()
print(fruits)

fruits.append('grape')  #append=add
print(fruits)
fruits.sort() #sort the elements in the list in alphabeticat order.
print(fruits)

fruits.sort(reverse=True)
print(fruits)

print(fruits.pop()) #retrieve the last element in the list and return it

print(fruits) 

fruits.remove('orange') #remove the first element 'orange' from the list
print(fruits)

fruits.clear()  #remove all the element in the list
print(fruits)

#copy() function of 'List'.Attention to the diffrence between ex1 and ex2

#ex1

original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()

# 要素を変更してみる
copied_list[0] = 10

print(original_list)  # 出力: [1, 2, 3, 4, 5]
print(copied_list)    # 出力: [10, 2, 3, 4, 5]


#ex2
original_list = [[1, 2], [3, 4]]
copied_list = original_list.copy()

# 内部のリストの要素を変更してみる
copied_list[0][0] = 10

print(original_list)  # 出力: [[10, 2], [3, 4]]
print(copied_list)    # 出力: [[10, 2], [3, 4]]






