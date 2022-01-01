# coding: utf-8
# 可変長引数をつかう

# 可変長引数なし
def log(message, values):
  if not values:
    print(message)
  else:
    values_str = ', '.join(str(x) for x in values)
    print(f'{message}: {values_str}')
log('My numbers are', [1, 2])
log('Hi there', [])

# 可変長引数あり
# スター引数をつけると可変長引数になる
# 関数の内部はそのままに呼び出す側がシンプルになる
def log2(message, *values):
  if not values:
    print(message)
  else:
    values_str = ', '.join(str(x) for x in values)
    print(f'{message}: {values_str}')
log2('My numbers are', 1, 2)
log2('Hi there')
# 引数ではなくイテレータで渡すことも可能
# ただし、タプルに変換されてしまうためイテレータの扱いに注意
# また、引数を増やす際に呼び出し側の修正が必要になるのでバグの要因になる
favorites = [7, 33, 99]
log2('Favorite colors:', *favorites)
