A, B = map(int, input().strip().split())
list=[]
sum=0
if A>=1 and B>=1:
  list.append(1)
  list.append(5)
if A>=1 and B==0:
  list.append(1)
elif A==0 and B>=1:
  list.append(5)
elif A<=0 and B<=0:
  print("Your input values were invalid.")
  exit()
for i in range(1,A+1):
  for j in range(1,B+1):
    sum=i+5*j
    list.append(sum)

list.sort()
out_list=set(list)
print(*out_list,sep="\n")
    