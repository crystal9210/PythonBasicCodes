# key=lenの場合
words=['apple','banana','kiwi','grape']
sorted_words=sorted(words,key=len)  #keyパラメータlen=length=長さ
print(sorted_words)

# key=ラムダ関数の場合
data=[{'name':'John','age':25},{'name':'Doe','age':30},{'name':'Jane','age':20}]
sorted_data2=sorted(data,key=lambda x:x['age'])