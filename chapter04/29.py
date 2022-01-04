# coding: utf-8

# 在庫
stock = {
  'nails' : 125,
  'screws' : 35,
  'wingnuts' : 8,
  'washers' : 24,
}
# 注文
order = ['screws', 'wingnuts', 'clips']

def get_batches(count, size):
  return count // size

# for,ifの組み合わせで注文に対する在庫数を算出
result = {}
for name in order:
  count = stock.get(name, 0)
  batches = get_batches(count, 8)
  if batches:
    result[name] = batches
print(result)

# 内包表記で短くかけるがifの条件がDRYに反する
found = {
  name: get_batches(stock.get(name, 0), 8)
  for name in order
  if get_batches(stock.get(name, 0), 8)
}
print(found)

# 項目10に出てきたウォルラス演算子で解決する
found = {
  name: batches
  for name in order
  if (batches := get_batches(stock.get(name, 0), 8))
}
print(found)