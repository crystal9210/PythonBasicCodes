#a test code 2 of nested List comprehension 

#ex1
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

ex1=[[row[i] for row in matrix] for i in range(4)]
print(ex1)

# ex2
#add:[row[i] for row in matrix]は、[row[i] for row in matrix]はネストリストの親リストmatrixからサブリストrowを取り出し、そのrowの要素のうち、ループ回数に一致するインデックス番号の要素を取り出す、ということ
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
# transposed = []
# for i in range(4):
#     # the following 3 lines implement the nested listcomp
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

print(transposed)

#additional operation
#zip：複数のイテラブル(リスト、ダブルなど)の要素をまとめてダブルの形で返す関数
a=[1,2,3]
b=['a','b','c']

result=list(zip(a,b))
print(result)

#*matrix：Pythonのアンパック演算子；リストやダブルなどのイテラブルの要素を案パックして、それぞれの要素を個別の引数として関数に渡すことができる
print(list(zip(*matrix)))   #zip関数にｙり生成されるイテラブルは変更を想定されていないため、変更不可能なイテラブルであるダブル；()のデータ構造により返される
# print(list)

#ex2 of 'zip' func ：ダブルを生成する元となるイテラブルの全てが持つ最低のインデックス番号までを処理する!→cの最後の要素を削除すると、zip関数により生成されるイテラブルは3個になる!(そのままは4個)
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]

zipped = list(zip(a, b, c))
print(zipped)  # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]



