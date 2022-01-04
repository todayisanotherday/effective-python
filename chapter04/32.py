# coding: utf-8

# 内包表記だとメモリに展開されてしまう
value = [len(x) for x in open('my_numbers.txt')]
print(value)

# ジェネレータ式を使う
# ()でくくるとイテレータが返却される
it = (len(x) for x in open('my_numbers.txt'))
print(next(it))
print(next(it))
print(next(it))

# ジェネレータ式は組み合わせが可能
# 作成したジェネレータを次のジェネレータ式に入れることで1つずつ処理できる
it = (len(x) for x in open('my_numbers.txt'))
roots = ((x, x**0.5) for x in it)
print(next(roots))
print(next(roots))
print(next(roots))