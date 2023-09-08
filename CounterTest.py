from collections import Counter

def judge_score(nums):
    # 各数値の出現回数をカウント
    counter = Counter(nums)
    
    # 出現回数で降順ソート
    sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    # 3回以上出現する数値が存在し、2つの数値が1回ずつ出現する場合
    if sorted_items[0][1] >= 3 and sorted_items[1][1] == 1 and sorted_items[2][1] == 1:
        return 'perfect'
    
    # 2つの数値が2回ずつ出現し、別の数値が1回出現する場合
    elif sorted_items[0][1] == 2 and sorted_items[1][1] == 2 and sorted_items[2][1] == 1:
        return '80点'
    
    # 上記の条件に当てはまらない場合
    else:
        return 'A cat eated a dog!!????'

while True:
    # 標準入力からスペース区切りの数値を読み取る
    try:
        nums = list(map(int, input("5つの整数をスペース区切りで入力してください (1-13の範囲): ").split()))
        
        # 入力された数値が5つで、1から13の間であるか確認
        if len(nums) != 5 or any(num < 1 or num > 13 for num in nums):
            raise ValueError("数値は1から13の範囲で5つ入力してください。")
        
        # スコアを判定して出力
        print(judge_score(nums))
        break  # 正しい入力がされたらループを終了
        
    except ValueError as e:
        print(e)

    
    