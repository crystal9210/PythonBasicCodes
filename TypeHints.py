# 'type hints' in Python is just annotations in other languages like Java, so they don't make no sense in codes.
from typing import List,Dict

name:str="cats"
list:List[int]=[10,6,8]

def make_sentence(name:str,list:List[int])->str:
  return str(list[1])+name

if __name__=='__main__':
  print(f'{make_sentence(name=name,list=list)} are having lunch now.')
  


