# 4つ以上の変数を取り出すときはアンパックしない
# 理由
# 順序の変換などがあったときにバグの原因になりやすい
# 1行が長くなってしまうので改行を余儀なくされる

import statistics

def get_stats(numbers):
  minimum = min(numbers)
  maximum = max(numbers)
  average = sum(numbers) / len(numbers)
  median = statistics.median(numbers)
  count = len(numbers)
  return minimum, maximum, average, median, count

numbers = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum, average, median, count = get_stats(numbers)
print(minimum, maximum, average, median, count)