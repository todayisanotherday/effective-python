# coding: utf-8

# tupleの指定を利用してグループにある数字のみ優先させたい
def sort_priority(values, group):
  def helper(x):
    if x in group:
      return (0, x)
    return (1, x)
  values.sort(key=helper)
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

# スコープ内の変数を書き換えたいがうまくいかない
# Falseが返されてしまう
# なぜなら値をセットする場合はhelper関数のスコープにfoundを新たにつくってしまうから
# スコープ処理バグの原因になる
def sort_priority2(values, group):
  found = False
  def helper(x):
    if x in group:
      fount = True
      return (0, x)
    return (1, x)
  values.sort(key=helper)
  return found
found = sort_priority2(numbers, group)
print(found)

# 代入でもスコープを外に出す方法
# nonlocalをつかう
# 見つけにくくなるというデメリットもある
def sort_priority3(values, group):
  found = False
  def helper(x):
    nonlocal found
    if x in group:
      found = True
      return (0, x)
    return (1, x)
  values.sort(key=helper)
  return found
found = sort_priority3(numbers, group)
print(found)

