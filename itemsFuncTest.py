fruits_count={
  'apple':5,
  'banana':3,
  'cherry':10
}

# itemsメソッドを使用して辞書の内容を表示
for fruit, count in fruits_count.items():
    print(f"There are {count} {fruit}s.")