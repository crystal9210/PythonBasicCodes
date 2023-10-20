# ランダムフォレストを用いたコード
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Irisデータセットを読み込む（分類タスク）
iris = load_iris()
X = iris.data  # 特徴量
y = iris.target  # ターゲット（クラス）
print(X)
print(y)

# データをトレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ランダムフォレスト(複数の決定木を組み合わせて予測をするアンサンブルモデル)分類器を作成
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# モデルをトレーニング
rf_classifier.fit(X_train, y_train)

# テストデータで予測
y_pred = rf_classifier.predict(X_test)

# 予測の精度を評価
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)  #1.0
