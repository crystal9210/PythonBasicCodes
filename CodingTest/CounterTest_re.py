from collections import Counter

def judge_score(nums):
  counter=Counter(nums)
  sorted_items=sorted(counter.items(),key=lambda x:x[1],reverse=True) #xはcounter.items()から取得されるタプルで、x[0]はその要素（キー）を、x[1]はその出現回数（値）を指します。このkey引数の指定により、ソートは要素の出現回数に基づいて行われます。
  
  if sorted_items[0][1]>=3 and sorted_items[1][1]==1 and sorted_items[2][1]==1:
    return 'perfect'
  elif sorted_items[0][1]==2 and sorted_items[1][1]==2 and sorted_items[2][1]==1:
    return '80点'
  else:
    return 'false(maybe?)'
  
while True:
  try:
    nums=list(map(int, input("5つの整数をスペース区切りで入力してください(1-13の範囲):").split()))
    if len(nums)!=5 or any(num<1 or num>13 for num in nums):
      raise ValueError('数値は1から13の範囲で5つ入力してください')
    
    print(judge_score(nums))
    break
  
  except ValueError as e:
    print(e)
    