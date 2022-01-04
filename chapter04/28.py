# coding: utf-8

# 内包表記の多重ループ
# 左から右に実行される
# for xが右端によるので若干わかりにくいようにおもったが、
# インデントが消えて一列になったと考えればわかりやすい
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]
flat = [x for row in matrix for x in row]
print(flat)

# 結果を2重にしたいばあい
# 行列と別々に処理していくイメージ
squared = [[x**2 for x in row] for row in matrix]
print(squared)

# ここまではまだ読みやすさがあったが、これ以上の多重化がされると複数行にまたがりわかりにくくなってくるので
# 3重以上はforとifによる書き方を検討する
