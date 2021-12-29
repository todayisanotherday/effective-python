# defaultdictは引数を渡せないため__missing__で欠損キーの場合の処理を記述する
# defaultdictでもlambdaで渡すこともできそうだが、初期化時に与えるものだから固定値しか入れられないと思う
# __missing__なら関数名ではなく処理そのものを渡せるため引数を渡せる


# dictを継承
class Pictures(dict):
  def open_picture(self, profile_path):
    try:
      return f'Value form {profile_path}'
    except OSError:
      print(f'Failed to open path {profile_path}')
      raise

  def __missing__(self, key):
    value = self.open_picture(key)
    self[key] = value
    return value

path = "path.txt"
pictures = Pictures()
# ここでpathをデフォルト値の判断のためのデータとして渡すことができている
handle = pictures[path]
print(handle)