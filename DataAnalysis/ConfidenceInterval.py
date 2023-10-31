import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
from scipy import stats



# 以下関数群の記述
def interval_test(parent_set, sample_size, sampling_count, alpha):
  """
  与えられた試行回数分、標本を抽出して信頼区間を可視化する

  Parameters
  ----------
  Args:
      parent_set (_type_): _description_
      sample_size (_type_): _description_
      sampling_count (_type_): _description_
      alpha (_type_): _description_
  """
  # figure
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)

  # 母集団が信頼区間内に入った回数
  interval_in_cnt=0
  # 母集団
  parent_mean=parent_set.mean()
  # 標本の平均、信頼区間下限・上限
  means=[]
  bottoms={}
  tops={}
  # サンプリング回数分繰り返す
  for i in range(sampling_count):
    # 標本取得
    sample=get_sample(parent_set, sample_size)
    # 標本平均
    sample_mean=sample.mean()
    means.append(sample_mean)
    # 信頼区間取得
    bottom, top=get_interval(sample, alpha)
    bottoms.append(bottom)
    tops.append(top)
    # 母集団平均が信頼区間内かどうか
    intrval_in=parent_mean>=bottom and parent_mean<=top
    # 母集団平均が信頼区間内に入った回数(信頼区間カウント)
    interval_in_cnt+=1 if interval_in else 0
    # 信頼区間内のばあいは青、信頼区間概の場合は垢とする
    fmt, ecolor=('bo','blue') if interval_in else ('ro', 'red')
    # 信頼区間内、区間概の凡例設定(それぞれ一回のみ表示)
    if interval_in_cnt ==1 and interval_in:
      # 初めて信頼区間内の場合(信頼区間カウントが1で信頼区間内)
      label='母集団平均が区間内'
    elif interval_in_cnt==i and not interval_in:
      # 初めて信頼区間概の場合(信頼区間カウント=標本回数-1で信頼区間外)
      label='母集団平均が区間外'
    else:
      label=''
    # 信頼区間をエラーバーとして表示
    ax.errorbar(i+1, sample_mean, [[sample_mean-bottom],[top-sample_mean]], fmt=fmt, capsize=4, label=label, ecolor=ecolor)



