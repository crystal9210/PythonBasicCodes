#a confirmation code of the iterable "set(集合)"
#集合の特徴：①同一の要素が存在しない　②可変だが、要素には不変の要素しか格納できない→集合の要素はハッシュ可能な(一意のハッシュ値を持つ)ことが必要；タプルもハッシュ可能
# 逆に、リスト、ディクショナリは内容が変更可能であるため、ハッシュ可能ではない

A={1,2,3,4,5}
B={4,5,6,7,8}

#交差：両方の集合に存在する要素　の確認
print(A&B)

#結合：いずかの集合に存在する要素
print(A|B)

#差：Aに存在し、Bに存在しない要素
print(A-B)

#対称差：AまたはBに存在し、両方には存在しない要素
print(A^B)

#add an element to the set
A.add(10)
A.add(10) #since a set only holds unique values, even if you try to add the same value multiple times, it will actually be added only once.
print(A)
A.add(100)
print(A)

#removes the specified element from the set
A.discard(10)
print(A)

A.clear()
print(A)  #output→set()

A.add(1)
A.add(2)

print(A.issubset({1,2,3}))  #whether A is included in {1,2,3}
print(A.issuperset({1,2,3}))

fruits={'apple','banana','cherry'}

if 'apple' in fruits:
  print('appleは集合に存在します')
else:
    print('appleは集合に存在しません')
  
if 'orange' in fruits:
  print('orangeは集合に存在します')
else:
    print('orangeは集合に存在しません')
