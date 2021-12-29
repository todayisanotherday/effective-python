# 欠損キーの処理
counters = {
  'pumpernickel': 2,
  'sourdough': 1,
}
key = 'wheat'

# in
if key in counters:
  count = counters[key]
else:
  count = 0
counters[key] = count + 1

# try-except
try:
  count = counters[key]
except KeyError:
  count = 0
counters[key] = count + 1

# getが一番シンプル
count = counters.get(key, 0)
counters[key] = count + 1

# valueがシンプルな値でなくlistの場合
# 存在しない場合にから配列を入れてから追加する例
votes = {
  'baguette': ['Bob', 'Alice'],
  'ciabatta': ['Coco', 'Deb']
}
key = 'brioche'
who = 'Elmer'
# get (セイウチ演算子も使うとよりシンプル)
if (names := votes.get(key)) is None:
  votes[key] = names = []
names.append(who)
# setdefault
# setなのに値を取得している点がわかりにくいという問題点
# setdefaultの値は複製でなく参照が直接代入されるので、使うたびにオブジェクトを用意する必要がある(使い回せない)
# 筆者はその問題点があるため、getかdefaultdictを推奨している
names = votes.setdefault(key, [])
names.append(who)

