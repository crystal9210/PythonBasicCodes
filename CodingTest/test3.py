# num_v=number of vegetables , num_m=number of meat
num_v, num_m, C, MAX=map(int, input().strip().split())
out=0
while (out+1)*(C+1)<MAX and out<=num_v and num_m>=C:
     out+=1
     num_m-=C
    #  print(num_meat) #挙動確認用


print(out)
