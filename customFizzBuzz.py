def custom_fizz_buzz(input_str):
    # 入力文字列をスペースで分割
    parts = input_str.split()

    # partsをキーに基づいて昇順に並べ替える前に、各要素を整数のキーと文字列の値に変換
    n=int(parts[-1])
    #print(n)    #ok.
    parts.pop() 
    # print(parts)
        
    # リストの要素尾を「:」で分割して辞書を作成
    result_dict={}
    for part in parts:
        key, value=part.split(":")
        result_dict[int(key)]=value
    
    #確認用の出力部分
    # print(result_dict)
    # for key in result_dict:
    #     print(result_dict[key])
    # print(sorted_dict[key])
    sorted_dict={k: result_dict[k] for k in sorted(result_dict,key=int)}
    #print(sorted_dict)  #ok.
    
    result=''
    # print(type(key))
    # 辞書内包表記(Dictionary Comprehension)
    for key in sorted_dict:
        if n%key==0: 
            result+=sorted_dict[key]
            
    return result if result else n

    
    
if __name__ == "__main__":
    # 標準入力からデータを読み取る
    input_data = input()
    print(custom_fizz_buzz(input_data))
    
    
    

    # キーに基づいて昇順に並べ替え
    # key_value_pairs.sort(key=lambda x: x[0] if isinstance(x, tuple) else int(x))

    # print(key_value_pairs)

    # print(parts)
    # 最後の数値を取得
    # n = int(parts[-1])
    # key_value_pairs.pop()
    # print(key_value_pairs)
    # key_value_pairs.sort(key=lambda x:x[0])
    # print(key_value_pairs)
    

    # 最大の約数を見つけるためのヘルパー関数
    # def get_largest_factor(val, factors):
    #     sorted_factors = sorted(factors, reverse=True)
    #     for factor in sorted_factors:
    #         if val % factor == 0:
    #             return factor
    #     return None

    # 結果の文字列を生成
    result = ''
    # 3と5の倍数かどうかを判定し、対応する文字列をresultに追記する
    # for key, value in key_value_pairs.:
    #   if n%key==0:
    #     result+=value
    
    # if result=='':
    #   result+=str(n)
      
    # return result
    


