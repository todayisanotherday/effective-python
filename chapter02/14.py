# 複雑なソート
# 数値や文字列のようにそのものでソートできないものをソートする
class Tool:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def __repr__(self):
    return f'Tool({self.name!r}, {self.weight})'

tools = [
  Tool('level', 3.5),
  Tool('hammer', 1.25),
  Tool('screwdriver', 0.5),
  Tool('chiel', 0.25),
]

print(tools)

# 単にソートはできない
try:
  tools.sort()
except Exception as e:
  print(e)

# keyを指定できる
print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('Sorted:  ', tools)
tools.sort(key=lambda x: x.weight)
print('Sorted:  ', tools)

# lowerで大文字小文字を無視などもできる
places = ['home', 'work', 'New York', 'Paris']
places.sort()
print(places)
places.sort(key=lambda x: x.lower())
print(places)

# 複数基準のソートtupleをつかう
power_tools = [
  Tool('drill', 4),
  Tool('circular saw', 5),
  Tool('jackhammer', 40),
  Tool('sander', 4),
]
saw = (5, 'circular saw')
jackhammer = (40, 'jackhammer')
assert not (jackhammer < saw)
drill = (4, 'drill')
sander = (4, 'sander')
assert drill[0] == sander[0]
assert drill[1] < sander[1]
assert drill < sander
# keyをtupleにする
power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)
power_tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
print(power_tools)
# 部分的にreverseにできる
power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)
power_tools.sort(key=lambda x: (x.name, x.weight))
print(power_tools)