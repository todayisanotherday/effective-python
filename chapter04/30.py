# coding: utf-8

# listでなくジェネレータで返す方法を検討

# listによる方法
# 単語の始まりのindexをリストで返す
# コードが読みづらい、配列操作部分のコードが重要な記述より多いため
def index_words(text):
  result = []
  if text:
    result.append(0)
  for index, letter in enumerate(text):
    if letter == ' ':
      result.append(index + 1)
  return result
address = 'Four score and seven years ago...'
result = index_words(address)
print(result)

# ジェネレータによる方法
# リスト生成に関する処理がなく反復のなかで返すようになっている
# 上から順繰りで返す様がわかりやすく、メモリの食いつぶしもなくなる
def index_words_iter(text):
  if text:
    yield 0
  for index, letter in enumerate(text):
    if letter == ' ':
      yield index + 1
print(list(index_words_iter(address)))
