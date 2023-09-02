#ハッシュ可能であることで、要素へのアクセスが高速化され、データの一意性やハッシュテーブルの安定性などのメリットが得られる

#ex1

# generate a dictionary that is able to be hashed
person={
  'name':'Taro',
  'age':30,
  'country':'Japan'
  }

#search the property
if 'name' in person:
  print(f"Name is :{person['name']}")

# ハッシュ不可能なキー（リスト）を持つディクショナリの作成を試みる
# これはエラーを発生させる
try:
    invalid_dict = {
        ["list_key"]: "value"
    }
except TypeError as e:
    print(f"Error: {e}")


#ex2

# ハッシュ可能なデータ（文字列、整数、タプルなど）のハッシュ値を取得
data = ["apple", 123, (10, 20)]

for item in data:
    print(f"Hash value of {item}: {hash(item)}")

# ハッシュテーブルを背景に持つディクショナリでの高速アクセスを確認
import time #本当は、モジュールの最上部にまとめて記述したほうがいいが、テストの可読性のためここに記述

# 大量のデータを持つディクショナリの作成
big_data = {i: f"value_{i}" for i in range(1, 1000001)}
# {
#     1: "value_1",
#     2: "value_2",
#     ...
#     1000000: "value_1000000"
# }



# ディクショナリへの高速アクセスのデモ
start_time = time.time()
print(big_data[999999])  # このアクセスは非常に高速に行われる
end_time = time.time()

print(f"Access time: {end_time - start_time:.6f} seconds")

