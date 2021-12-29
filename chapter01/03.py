# coding: utf-8

# bytes
a = b'h\x65llo'
print(list(a))
print(a)

# bytes(符号系)
a = 'a\u0300 propos'
print(list(a))
print(a)

# to_str
def to_str(bytes_or_str):
  if isinstance(bytes_or_str, bytes):
    value = bytes_or_str.decode('utf-8')
  else:
    value = bytes_or_str
  return value
print(repr(to_str(b'foo')))
print(repr(to_str('bar')))

# 同じ型でしか結合できない
print(b'one' + b'two')
print('one' + 'two')
try:
  a = 'one' + b'two'
  print(a)
except Exception as e:
  print(e)

# 同じ型でしか比較できない
assert b'red' > b'blue'
assert 'red' > 'blue'
try:
  assert 'red' > b'blue'
except Exception as e:
  print(e)
try:
  assert b'blue' > 'red'
except Exception as e:
  print(e)

# 違う形同士の評価値はFalseになる
print('foo' == 'foo')
print(b'foo' == b'foo')
print(b'foo' == 'foo')

# bytesでもstrでもフォーマット文字列は対応
print('red %s' % 'blue')
print(b'red %s' % b'blue')
# bytesのフォーマットにstrを渡せない(エンコードがわからないため)
try:
  print(b'red' % 'blue')
except Exception as e:
  print(e)
# 逆にstrのフォーマットにbytesはいれられるがうまくいかない
# 置き換える際にb'blue'となってしまう
print('red %s' % b'blue')

