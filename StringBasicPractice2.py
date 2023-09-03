a='try nukko me.'
print(a.startswith('try'))
print(a.find('nu')) #前から何文字目かを出力
print(a.rfind('o')) #後ろから何文字目に見つかるかを出力

print(a.capitalize()) 
print(a.title())
print(a.upper())
print(a.lower())
print(a.replace('nukko','innu'))

#f-strngs;こっちの方がformatより処理が早い
a=100
print(f'a is {a}')

#format
print('a is {0} {1} {2}'.format('2','3','6'))
print('a is {0} {1} {2}; {2} {1} {0}'.format('2','3','6'))
print('a is {0} {1} {2}')

