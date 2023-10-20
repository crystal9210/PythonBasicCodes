# 主成分分析の基本確認用
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np


data = [
    [160, 50, 30],
    [165, 55, 35],
    [170, 60, 40],
    [175, 65, 45],
    [180, 70, 50]
]


scaler=StandardScaler()
# リストからNumPy配列に変換
X=np.array(data)
standardized_data=scaler.fit_transform(X)
# 主成分分析を実行
pca=PCA()
principal_components=pca.fit_transform(standardized_data)

# 標準化されたデータの表示
print('標準化されたデータ：')
print(standardized_data)

# 主成分の表示
print("各主成分の寄与率：",pca.explained_variance_ratio_)   #[1.00000000e+00 1.38345477e-32 3.61696216e-64]→第一主成分がほとんどデータの値を決定する

# 主成分スコアを表示
print("主成分スコア：")
print(principal_components)

