import pandas as pd

# サンプルデータの生成
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 6, 7, 8, 9],
    'C': [9, 8, 7, 6, 5],
    'D': [1, 3, 5, 7, 9]
}
df = pd.DataFrame(data)

# ilocを使用したデータの選択
print(df.iloc[2])         # 3行目のデータ
print(df.iloc[[0, 3]])    # 1行目と4行目のデータ
print(df.iloc[1:4, 1:3])  # 2〜4行目のBとC列のデータ
