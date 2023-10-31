# KaggleのチュートリアルなのでKaggleのクラウド環境で行う
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melbourne_file_path = (
    "/kaggle/input/testdatas/melb_data.csv"  # ''内にはクラウド環境のデータセットのパスを指定
)
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data.describe()

# pandasライブラリのDataFrameオブジェクトに対し、columnsメソッドを呼び出すと
# データフレームのカラムの名前;データフレーム内の各列に付けられた識別子やラベルの
# 名前を出力することができる
print(melbourne_data.columns)

# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)
# We'll learn to handle missing values in a later tutorial.
# Your Iowa data doesn't have missing values in the columns you use.
# So we will take the simplest option for now, and drop houses from our data.
# Don't worry about this much for now, though the code is:

# dropna drops missing values (think of na as "not available")
filtered_melbourne_data = melbourne_data.dropna(axis=0)

y = filtered_melbourne_data.Price

melbourne_features = [
    "Rooms",
    "Bathroom",
    "Landsize",
    "BuildingArea",
    "YearBuilt",
    "Lattitude",
    "Longtitude",
]

X = filtered_melbourne_data[melbourne_features]

print(X.describe())

print(X.head())  # 3と5の行番号（インデックス）はデータフレーム内で示されていないため、データが欠損しているか、削除されている可能性あり

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))


# 以下、モデルの性能検証
# ここで指標は最も簡易的なものの一つ、MAE;Mean Absolute Error;error=actual-predictedを使う
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)


# 検証データを持ちいてモデルの性能を評価
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
