def judge_result(midterm, final):
  if final <=60 or (midterm + final) <=100:
    if final <=60 and (midterm+final) <=100:
      return 'fail'
    else:
      return 'reexamination'
  else:
    return 'pass'
  
def main():
  n=int(input().strip())
  for _ in range(n):
    midterm, final =map(int, input().strip().split())
    print(judge_result(midterm,final))
    
if __name__=="main":
  main()