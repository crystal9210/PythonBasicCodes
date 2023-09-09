import numpy as np  #数値計算を効率的にするためのライブラリ。配列や行列の操作に非常に強力
from sklearn.linear_model import LinearRegression #機械学習ライブラリ；分類、回帰、クラスタリングなど、さまざまなアルゴリズムを提供
import matplotlib.pyplot as plt
import japanize_matplotlib

# データの定義→NumPy配列は高効率的かつ多機能で、機械学習のタスクに適している
X = np.array([50, 70, 90, 110, 130]).reshape(-1, 1)  # 家の広さ
y = np.array([200, 270, 350, 430, 510])  # 家の価格

# 線形回帰モデルの作成
model = LinearRegression()  #線形回帰モデルのインスタンスの生成→最小二乗法の利用、線形回帰モデルは基本的には、y=wX+bの数式に基づいている；wは特徴量に対する重み(モデルの係数)、yは切片(バイアス)
model.fit(X, y) #データX,Yを使ってモデルを学習させている→モデルは、あらかじめインポートしたLinearRegressionライブラリからのデータ構造によるインスタンスおよび、定義データX,yにより自動的にモデルに対する関係式を導出、生成する

# 予測
house_size_new = np.array([[10]])
predicted_price = model.predict(house_size_new)
print(f"家の広さが{house_size_new[0][0]}平方メートルの場合、予測価格は{predicted_price[0]:.2f}百万円です。")

# グラフの描画
plt.scatter(X, y, color='blue', label='実際のデータ')
plt.plot(X, model.predict(X), color='red', label='予測の回帰直線')
plt.title('家の広さと価格の関係')
plt.xlabel('家の広さ（平方メートル）')
plt.ylabel('家の価格（百万円）')
plt.legend()
plt.show()


# add：
# ①NumPyはPythonでの数値計算を効率的に行うためのライブラリ。大量のデータを効率的に操作でき、高速な数学的計算をサポートしている。ベクトル計算や行列計算など、機械学習タスクで頻繁に使用される

# ②l15の処理：それらをmodelに学習させる際には、インデックス番号が二つのデータ配列から一致する者同士を順に抽出して適応させることで生成する、という認識でいいですか。
# →
# はい、その認識は正しいです。Xとyのデータは対応関係にあります。例えば、Xの最初の要素（家の広さ）は、yの最初の要素（その家の価格）に対応しています。学習の際、この対応関係を基にモデルが重みとバイアスを調整します。

# ③predicted_price = model.predict(house_size_new)に関しては、その際に作成したモデルに対して、ライブラリに標準搭載されている、predictメソッドが学習したモデルから自動的に適切な値を計算するためのメソッド、という認識で正しいですか。

# はい、その認識は正確です。predictメソッドは、学習済みのモデル（ここでは線形回帰モデル）を使用して、新しい入力データ（ここではhouse_size_new）に対する出力（予測価格）を計算します。このメソッドは、モデルが学習中に見つけた重みとバイアスを使用して、入力データから予測を生成します。