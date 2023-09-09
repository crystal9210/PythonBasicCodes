def count_conbinations(cards,k):
  count=0
  n=len(cards)
  for i in range(n):
    for j in range(i+1,n):
      for l in range(j+1,n):
        if cards[i]+cards[j]+cards[l]==k:
          count+=1
  return count

# 標準入力からnとkを受け取る
n, k=map(int,input().split())

# 標準入力からカードの数字を受け取る
cards=list(map(int,input().split()))

# 結果を出力
print(count_conbinations(cards,k))
