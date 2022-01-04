# conding: utf-8

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

# メモリで渡す
visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages)

# ファイルで渡す
# 最初のsumでジェネレータが終わってしまうのでうまくいかない
# []
it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)

# 全データをリストに変更して盛り込んでいる
# listに変換しているのでうまくいくが結局変換されてしまう
def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)

# リスト変換ではなくジェネレータを渡す
# メモリが圧迫することがなくなるがラムダを渡すことがコードの見た目上大変
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result
path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)

# イテレータを使うと動く
# これでは動かないように思うがsumやforで再度イテレータが渡されることを保証する
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path
    
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)

# イテレータであることを確認する
from collections.abc import Iterator
def normalize_defensive(numbers):
    # 2通りの方法がある
    # if iter(numbers) is numbers:
    #     raise TypeError('Must supply a container.')
    if isinstance(numbers, Iterator):
        raise TypeError('Must supply a container.')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result