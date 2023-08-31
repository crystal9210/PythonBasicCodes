# Pythonでパフォーマンスチューニング例コード
# チューニング前と後の実行時間をそれぞれ計測し出力
import time

# 非効率な例
start_time1=time.time()

result =[]
for i in range(10**6):
  result.append(i*2)

end_time1=time.time()
execution_time1=end_time1 - start_time1
print("Execution time:", execution_time1,"seconds")

# 効率的な例
start_time2=time.time()

result=[i*2 for i in range(10**6)]

end_time2=time.time()
execution_time2=end_time2 - start_time2
print("Execution time:", execution_time2,"seconds")



