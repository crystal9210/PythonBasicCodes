# 必要なライブラリをインポート
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# サンプルデータを作成
messages = [
    ("スパム", "最新のiPhoneを手に入れよう！"),
    ("ハム", "昼食に何を食べるか考えています。"),
    ("ハム", "今週末、映画を観に行こうと思っています。"),
    ("スパム", "お金を稼ぐ方法を教えます！"),
]

# データセットを特徴量ベクトルXとラベルyに分類
X = [message[1] for message in messages]
y = [message[0] for message in messages]
print(X)
print(y)

# テキストデータをベクトル化
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)
print(X)

# 列番号から単語を取得
feature_names = vectorizer.get_feature_names_out()

# 列番号と対応する単語を表示
for i, word in enumerate(feature_names):
    print(f"列番号 {i}: {word}")
# 辞書の単語とそのインデックスを表示
print(vectorizer.vocabulary_)

# データセットをトレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 単純ベイズ分類器を作成
classifier = MultinomialNB()

# モデルをトレーニング
classifier.fit(X_train, y_train)

# テストデータで予測
y_pred = classifier.predict(X_test)

# モデルの性能評価
accuracy = accuracy_score(y_test, y_pred)
print("正解率：", accuracy)

# クラスごとの詳細な性能評価
print(classification_report(y_test, y_pred))
