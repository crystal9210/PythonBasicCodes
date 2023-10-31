# Decision Tree Regression;決定木回帰モデル

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt # プロット及びデータの可視化のためのライブラリ
import pandas as pd # データ分析および分析のためのライブラリ
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values  # values:datasetデータフレームから選択されたデータをNumPy配列として取得するためのメソッド

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)  # test_size:データセット全体からテスト用データセットのサイズをどの割合で分割するかを指定、

# Training the Decision Tree Regression model on the Training set
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Evaluating the Model Performance
r2_score_result = r2_score(y_test, y_pred)
print("R-squared (R2) Score:", r2_score_result)

# 乱数生成のシード値とは:乱数生成器の初期化パラメータで、乱数生成の規則を指定するための値。
# 【比較】
# random_state:乱数生成器から乱数を生成する際に乱数生成器に渡すパラメータ;特定の関数やメソッドにおいて、乱数群生成のランダム性を制御するための値。
# ☆上記二つのパラメータを利用するメリット：
# 上記二つの値を組み合わせて用いることで一定水準以上の任意性を保証でき、
# かつ、二つの値を同じ値に設定することでエラー対処の際の再現性などが保証できる。
