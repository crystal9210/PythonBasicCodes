import numpy as np

# シード値を設定
np.random.seed(42)

# 乱数を生成;シード値が一緒なら同じ乱数が生成される
random_numbers=np.random.rand(5)

print(random_numbers)

# memo:乱数生成の際のシード(seed:種→乱数を生成するときの種のイメージ。同じ種からは同じ乱数値群が生成される;任意性を持たせたいときは指定せず乱数生成を行う)値は整数値であることが一般的。ランダム性の初期化に使用され、同じシード値を指定すると同じ乱数が生成される。
