# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os

for dirname, _, filenames in os.walk("/kaggle/input"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
train = pd.read_csv("../input/titanic/train.csv")
test = pd.read_csv("../input/titanic/test.csv")
print(train)
print(test)
print(test.dtypes)
train.isnull().sum()
print(test.dtypes)
# 特徴量Sexを数値にエンコード
le = LabelEncoder()
train["Sex"] = le.fit_transform(train["Sex"])
# エンコード前とエンコード後の各データのペアを確認
for index, label in enumerate(le.classes_):
    print(f"{label}:{index}")
# 使用する特徴量とターゲットを指定
features = ["Pclass", "Sex", "Fare"]
target = "Survived"
x = train[features]
y = train[target]
# ロジスティック回帰モデルを初期化
model = LogisticRegression(max_iter=1000, random_state=42)
# まずモデルに全訓練データで訓練する
model.fit(x, y)
# testデータを用いてSurvivedを予測
test["Sex"] = le.fit_transform(test["Sex"])
features = ["Pclass", "Sex", "Fare"]
target = "Survived"
# test_x=test[features]
# 下のpredict()関数を使おうとしたら予測元の特徴量に欠損値があるらしく、一旦それを予測する前処理
# 長くなりそう...
pre_le = LabelEncoder()
# Fareがnullでないデータを学習データとして抽出
train_data = test.dropna(subset=["Fare"])
# PclassとSexを特徴量として、Fareを目的変数として学習
pre_x = train_data[["Pclass", "Sex"]]
pre_y = train_data["Fare"]

pre_model = DecisionTreeRegressor(random_state=42)

# FareがnullのデータのFareを予測
null_fare_data = test[test["Fare"].isnull()]
pre_train = null_fare_data[["Pclass", "Sex"]]
pre_model.fit(pre_x, pre_y)
predicted_fares = pre_model.predict(pre_train)

# 予測されたFareを元のデータフレームに代入
test.loc[test["Fare"].isnull(), "Fare"] = predicted_fares
# testの各データに対する特徴量'Survived'の予測
test_x = test[features]
predictions = model.predict(test_x)
# Kaggleのコンペページに提出できる形式に予測データをまとめたファイルの生成
output = pd.DataFrame({"PassengerId": test.PassengerId, "Survived": predictions})
output.to_csv("submission.csv", index=False)
print("Your submission was successfully saved!")
