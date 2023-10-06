def judge_result(midterm, final):
  if final <=60 or (midterm + final) <=100:
    if final <=60 and (midterm+final) <=100:
      return 'fail'
    else:
      return 'reexamination'
  else:
    return 'pass'
  
def main():
  n=int(input().strip())  #ユーザからの入力が'5'なら正常に処理が終了するが、'5 'の時は空白が文字列の一部として認知されエラーの原因となる。
  for _ in range(n):
    while True:
      try:
        midterm, final =map(int, input().strip().split())
        if midterm < 0 or midterm >= 100 or final < 0 or final >= 100:
          print("Midterm and final scores must be between 0 and 100. Please try again.")
          continue
        print(judge_result(midterm,final))
        break #正しい入力が得られたらループを抜ける
      except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
    
if __name__=="__main__":
  main()