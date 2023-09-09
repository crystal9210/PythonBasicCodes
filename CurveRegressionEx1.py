import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import japanize_matplotlib

# サンプルデータの生成（1年分の日数とそれに対応する気温）
days = np.linspace(0, 365, 365)  # 1年間の日数
# sin関数を使用して周期的な気温変動を模倣
temps = 20 + 10 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, 2, days.size)  # 平均気温20℃、変動幅10℃

# 多項式特徴量の生成（3次の多項式）
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(days.reshape(-1, 1))

# 多項式回帰モデルの学習
model = LinearRegression()
model.fit(X_poly, temps)

# 予測の実施
temps_pred = model.predict(X_poly)

# グラフの描画
plt.scatter(days, temps, color='blue', s=10, label='実際の気温')
plt.plot(days, temps_pred, color='red', label='予測の曲線')
plt.xlabel('日数')
plt.ylabel('気温 (℃)')
plt.legend()
plt.title('1年間の気温の変動とその予測')
plt.show()
