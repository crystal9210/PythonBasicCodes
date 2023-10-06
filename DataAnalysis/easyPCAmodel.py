import numpy as np 

# サンプルデータ
data = np.array([
    [1.1, 2],
    [2.1, 3],
    [3.1, 4],
    [4.1, 5],
    [5.1, 6]
])

# データの標準化
mean=np.mean(data,axis=0) #各列の平均値を計算、結果が3.0などの整数の場合、3.というように出力。3.1のときは3.1と出力
std_dev=np.std(data,axis=0) #各列の標準偏差を計算
standardized_data=(data-mean)/std_dev #データの標準化；データを平均値で中心化し、標準偏差でスケーリングすることでデータを標準化する。これにより各特徴量が平均0、分散1となる。よって、異なる項目のデータでもその大小を比較することができるようになる

# 共分散行列の計算
covariance_matrix=np.cov(standardized_data, rowvar=False)

# 固有値分解；引数に共分散行列を指定して、線形代数の固有値とそれに対応する固有ベクトルを求め、それぞれ変数に代入
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

# 主成分の選択（例: 最大の固有値に対応する主成分(ベクトル)を選択）
max_eigenvalue_index = np.argmax(eigenvalues)   #eigenvalues配列のうち、最大の値を格納しているインデックス番号を抽出・格納
principal_component = eigenvectors[:, max_eigenvalue_index] #第二引数：eigenvectorsのうち、max_eigenvalue_indexのインデックスに一致する要素を指定、
# 第一引数：第二引数で指定したインデックスに一致する列全体を取り出すことを指示

# 主成分スコアの計算
principal_component_scores = np.dot(standardized_data, principal_component)

print(mean)
print(std_dev)
print(covariance_matrix)    
#[[1.25 1.25]
# [1.25 1.25]]
print(standardized_data)
# [[-1.41421356 -1.41421356]
#  [-0.70710678 -0.70710678]
#  [ 0.          0.        ]
#  [ 0.70710678  0.70710678]
#  [ 1.41421356  1.41421356]]
print(eigenvalues)  #データポイントが2次元なので、共分散行列は2*2となり、よって重複を含め固有値は2個求められる
print(eigenvectors) #データポイントが2次元→2*2の共分散行列→固有ベクトルも2次元*2
print(principal_component)
# [0.70710678 0.70710678]
print(principal_component_scores)
# [-2. -1.  0.  1.  2.] 浮動小数点以下の桁数が非常に小さい場合結果が見やすくするために四捨五入されることがある→元のデータ数5は保持
print(max_eigenvalue_index)
print(principal_component_scores)
