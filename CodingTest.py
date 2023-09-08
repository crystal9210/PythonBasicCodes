n = int(input().strip())

for i in range(n):
    midterm, final = map(int, input().strip().split())
    
    if final <= 60 or (midterm + final) <= 100:
        if final <= 60 and (midterm + final) <= 100:
            print("fail")
        else:
            print("reexamination")
    else:
        print("pass")
