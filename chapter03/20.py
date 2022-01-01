# Noneでなく例外を送出する
# 悪くはないが呼び出し側にifで1回は判断させる必要が生じる
# ifの中の判断でNoneを使おうとした倍に0もFalseになるのでバグの原因にもなる
# 例外にすると型が1つに限定されるので静的チェックできるようになるという利点もある

# Noneで動作する例
def devide(a, b):
  try:
    return a/b
  except ZeroDivisionError:
    return None 
result = devide(1, 0)
if result is None:
  print("invalid...")


# 0が結果でNoneの場合処理したいコードだとバグの原因にもなる
# (is Nonedでいい気がするが)
result = devide(0, 10)
if not result:
  print("invalid...")


# tupleにして結果を返す方法もあるが無視できてしまう
def devide2(a, b):
  try:
    return True, a/b
  except ZeroDivisionError:
    return False, None
successed, result = devide2(1, 0)
if not successed:
  print("invalid...")


# 例外にすると他関数も含めてまとめてキャッチできる
# 型にNone型が返されることがなくなるため静的型チェック,docstringが有効になる
def devide3(a: float , b: float) -> float:
  """Devided a by b.

  Args:
      a (float): [description]
      b (float): [description]

  Raises:
      ValueError: [description]

  Returns:
      float: [description]
  """
  try:
    return a/b
  except ZeroDivisionError:
    raise ValueError('Invalid inputs')
try:
  result = devide3(2, 0)
except ValueError:
  print("invalid...")
else:
  print(f'Result is {result}')
