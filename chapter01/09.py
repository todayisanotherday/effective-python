# forループのelseは使わない
# elseはループが完了したら実行される構文だが名前が紛らわしいため
for i in range(3):
  print("Loop", i)
else:
  print("Else")

# breakされると実行されない
for i in range(3):
  print("LOOP", i)
  if i == 1:
    break
else:
  print('Else')
  
# から配列ならループがなくてもElseが呼ばれる
for x in []:
  print("Never runs")
else:
  print("Else")

# 本来どういうときに使われる？
# 特定の条件が揃ったときにbreakさせ何も起きなければelseを呼ぶ
a = 4
b = 9
for i in range(2, min(a,b) + 1):
  print('Testing', i)
  if a % i == 0 and b % i == 0:
    print('Not coprime')
    break
else:
  print('Comrime')
# しかしこのように書かなくても関数に分けたほうが明瞭になる
def coprime(a, b):
  for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
      return False
  return True
assert coprime(4, 9)
assert not coprime(3, 6)

# 代入演算子
# ifの前に変数を用意せずに条件部分で代入できる
def orange(x):
  return x
if x := orange(1):
  print(x)
if x := orange(0):
  print(x)