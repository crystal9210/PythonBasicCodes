import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    ['これ', 'は', '最初', 'の', 'ドキュメント', 'です', '。'],
    ['この', 'ドキュメント', 'は', '2', '番目', 'の', 'ドキュメント', 'です', '。'],
    ['そして', '、', 'これ', 'は', '3', '番目', 'の', 'もの', 'です', '。'],
    ['これ', 'は', '最初', 'の', 'ドキュメント', 'です', 'か', '?']
]
vectorizer = CountVectorizer(analyzer=lambda x: x)

vec = vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names_out()
df = pd.DataFrame(vec.toarray(), columns=feature_names)
