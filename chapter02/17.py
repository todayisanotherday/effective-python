# dictのvalueがset
# やりたいこと：ここに新たな集合を作成する
visits = {
  'Mexico': {'Tulum', 'Puerto Vallarta'},
  'Japan': {'Hakone'}
}

# setdefaultで実現できる
visits.setdefault('France', set()).add('Arles')

# getだとちょっと長い
if (japan := visits.get('Japan')) is None:
  visits['Japan'] = japan = set()
japan.add('Kyoto')
print(visits)

# 直接辞書をいじるのではなくクラスでラップすると使いやすい
class Visits:
  def __init__(self):
    self.data = {}
  
  def add(self, country, city):
    city_set = self.data.setdefault(country, set())
    city_set.add(city)
visits = Visits()
visits.add('Russia', 'Yekaterinburg')
visits.add('Tanzania', 'Zanzibar')
print(visits.data)

# defaultdictを使う
# defaultdict自身の機能でキーがない場合にデフォルト値を入れてくれる
from collections import defaultdict
class Visits2:
  def __init__(self):
    self.data = defaultdict(set)
  
  def add(self, country, city):
    self.data[country].add(city)

visits = Visits2()
visits.add('Russia', 'Yekaterinburg')
visits.add('Tanzania', 'Zanzibar')
print(visits.data)