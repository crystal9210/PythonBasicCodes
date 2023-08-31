# 1+2+3+... +1000000の実行時間を計測するためのプログラム
import time

start_time=time.time()

k=0

for x in range(10**6):
  k+=x

print(k)

end_time=time.time()
execution_time=end_time-start_time
print("Execution time:", execution_time,"seconds")
# 499999500000
# Wall time: 312 ms