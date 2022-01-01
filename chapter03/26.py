# functools.wraps

# 関数をの引数、結果を出力する関数
# !rは
def trace(func):
  """こちらはtrace関数です"""
  def wrapper(*args, **kwargs):
    """こちらはwrapper関数です"""
    result = func(*args, **kwargs)
    print(f'{func.__name__}({args!r},{kwargs!r}) '
          f'-> {result!r}')
    return result
  return wrapper

# デコレータとして渡す
@trace
def fibonacci(n):
  """こちらはフィボナッチ関数です"""
  if n in (0, 1):
    return n
  return (fibonacci(n-2) + fibonacci(n-1))

fibonacci(4)
# 関数をそのまま出力するとtraceを関数として返す
# デコレータでラップされているため
# デバッグをする際にこの振る舞いが邪魔をすることがある
print(fibonacci)
# 例えば関数の説明を出力するhelp関数が使えない
# viが起動するため一時コメントアウト
# help(fibonacci)


# 解決法：functoolsのwrapsヘルパー関数を使う
# 関数情報を隠されずに複製される
# -> デコレータを助けるデコレータ
from functools import wraps
def trace2(func):
  """こちらはtrace2関数です"""
  @wraps(func)
  def wrapper(*args, **kwargs):
    """こちらはwrapper関数です"""
    result = func(*args, **kwargs)
    print(f'{func.__name__}({args!r},{kwargs!r}) '
          f'-> {result!r}')
    return result
  return wrapper

# 同様にデコレータとして渡す
@trace2
def fibonacci2(n):
  """こちらはフィボナッチ関数2です"""
  if n in (0, 1):
    return n
  return (fibonacci(n-2) + fibonacci(n-1))
fibonacci2(4)
# fibonacciとして出力される
print(fibonacci2)