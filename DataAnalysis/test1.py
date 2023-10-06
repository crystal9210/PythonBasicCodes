# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# read datas
data=pd.read_csv('sales_data.csv')

# comfirm by outputting first some lines of the data
print(data.head())


# data cleaning and preprocessing
# 血管地のチェックと保管
data.fillna(0,inplace=True)
# 異常値の修正(価格が0未満の場合を考える)
data['price']=data['price'].apply(lambda x:max(x,0))
# 重複データの削除
data.drop_duplicates(inplace=True)

# データ探索と可視化
# 売上の時間の変化を可視化
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['sales'])
plt.xlabel('日付')
plt.ylabel('売上')
plt.title('売上の時間の変化')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# データ分析
# 季節性の影響を評価するために、月ごとの平均売上を計算
monthly_sales = data.groupby(data['date'].dt.month)['sales'].mean()

# 月ごとの平均売上を可視化
plt.figure(figsize=(8, 5))
monthly_sales.plot(kind='bar')
plt.xlabel('月')
plt.ylabel('平均売上')
plt.title('月ごとの平均売上')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()


