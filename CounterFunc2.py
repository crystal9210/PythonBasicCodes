from collections import Counter
# サンプルのリスト

list=[1,2,3,3,3,3,3,44,6,6,7,356,35,3,3,6,7,6,6,6,1,1]

# 要素数の出現回数をカウント
element_counts=Counter(list)

# 各要素の祝言回数分だけ☆を表示
for element, count in element_counts.items():
  print(f"要素{element}:{'☆'*count}")
