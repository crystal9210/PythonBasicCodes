from collections import Counter

# サンプルのリスト
list=[1,2,3,4,3,3,2,2,2,5,56,77,3,2,2,1]

# 要素数の出現回数をカウント
element_counts=Counter(list)

# 結果の表示
for element, count in element_counts.items():
  print(f"要素{element}の出現回数：{count}")