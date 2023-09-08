# code sample of algorithm
# √3の平方根を誤差0.01以内で求めるプログラム(√3=1.732...)

# 反復法...計算回数：175回
x=0
while x**2<=3:
  x=x+0.01
print(x)  #1.740...


# 二分法...計算回数：9回
a=0
b=3
while b-a >0.01:
  c=(a+b)/2
  if c**2>3:
    b=c
  else:
    a=c
print(a)  #1.728...


#ニュートン法...計算回数：3回
x=3
while abs(3-x**2)>0.01:
  x=(x**2+3)/(2*x)
print(x)  #1.732...

  




