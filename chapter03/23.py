def remainder(number, divisor):
  return number % divisor

assert remainder(20, 7) == 6

# 特に指定しなくてもキーワードを引数で指定できる
assert remainder(20, divisor=7) == 6
assert remainder(number=20, divisor=7) == 6
assert remainder(divisor=7, number=20) == 6

# dictを引数として展開できる
kw_args = {
  'number' : 20,
  'divisor': 7,
}
assert remainder(**kw_args) == 6

# 複数展開
number = {
  'number' : 20,
}
divisor = {
  'divisor': 7,
}
assert remainder(**number, **divisor) == 6

# デフォルト引数
def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
  return ((weight_diff * units_per_kg) / time_diff) * period
print(f'{flow_rate(12, 60)} kg per second')
