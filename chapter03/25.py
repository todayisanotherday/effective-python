# 振る舞いを変えるような引数はデフォルト値を設定しないと引数が混乱する
def safe_division(number, divisor, ignore_overflow,
                  ignore_zero_division):
  try:
    return number / divisor
  except OverflowError:
    if ignore_overflow:
      return 0
    else:
      raise
  except ZeroDivisionError:
    if ignore_zero_division:
      return float('inf')
    else:
      raise
print(safe_division(1.0, 10**500, True, False))
print(safe_division(1.0, 0.0, False, True))

# 改善
# オプションを指定しなくてもこれまでどおりの振る舞いをする
def safe_division_b(number, divisor,
                  ignore_overflow=False,
                  ignore_zero_division=False):
  try:
    return number / divisor
  except OverflowError:
    if ignore_overflow:
      return 0
    else:
      raise
  except ZeroDivisionError:
    if ignore_zero_division:
      return float('inf')
    else:
      raise
print(safe_division_b(1.0, 10**500, ignore_overflow=True))
print(safe_division_b(1.0, 0.0, ignore_zero_division=True))
print(safe_division_b(1.0, 10**500, True, False))
print(safe_division_b(1.0, 0.0, False, True))

# 改善
# オプションと位置引数を明確に分ける
def safe_division_c(number, divisor, *,
                  ignore_overflow=False,
                  ignore_zero_division=False):
  try:
    return number / divisor
  except OverflowError:
    if ignore_overflow:
      return 0
    else:
      raise
  except ZeroDivisionError:
    if ignore_zero_division:
      return float('inf')
    else:
      raise
print(safe_division_c(1.0, 10**500, ignore_overflow=True))
print(safe_division_c(1.0, 0.0, ignore_zero_division=True))
try:
  safe_division_c(1.0, 0.0)
except ZeroDivisionError:
  print('OK')

# 改善
# さらに位置専用引数でしか呼び出せないことを明示することで名前付き引数を制限する 
def safe_division_d(number, divisor, /, *,
                  ignore_overflow=False,
                  ignore_zero_division=False):
  try:
    return number / divisor
  except OverflowError:
    if ignore_overflow:
      return 0
    else:
      raise
  except ZeroDivisionError:
    if ignore_zero_division:
      return float('inf')
    else:
      raise
print(safe_division_d(1.0, 10**500, ignore_overflow=True))
print(safe_division_d(1.0, 0.0, ignore_zero_division=True))
# 位置専用引数にキーワードを指定すると例外が発生する
try:
  safe_division_d(number=1.0, divisor=1.0)
except Exception as e:
  print(e)