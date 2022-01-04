# coding: utf-8

# 内包表記

# 要素ごとに2乗するリスト
a = list(range(1, 10))

# for文による方法
squares = []
for x in a:
  squares.append(x**2)
print(squares)

# mapによる方法
squares = map(lambda x: x**2, a)
print(squares)

# 内包表記による方法
# 見た目がシンプルでわかりやすい
squares = [x**2 for x in a]
print(squares)

# ここから偶数だけ残すことを考える

# for文による方法
# 複雑になってくると逆に一番わかりやすい気もしてくる
squares = []
for x in a:
  if x % 2 == 0:
    squares.append(x**2)
print(squares)

# map, filterによる
even_squares = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print(even_squares)

# 内包表記による
even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)

# dictもできる
even_squares_dict = { x: x**2 for x in a if x % 2 == 0 }
print(even_squares_dict)

# setもできる
threes_cubed_set = { x**3 for x in a if x % 3 == 0 }
print(threes_cubed_set)

# map, filterでもできるがネストがちょっとつらい
# tupleのlistをdictにわたす
alt_dict = dict(map(lambda x: (x, x**2), filter(lambda x: x % 2 == 0, a)))
print(alt_dict)
# mapの結果のiterableをsetに変換
alt_set = set(map(lambda x: x**3, filter(lambda x: x % 3 == 0, a)))
print(alt_set)
