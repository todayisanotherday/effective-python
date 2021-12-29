# 先頭2つを取り出す
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest = car_ages_descending[:2]
others = car_ages_descending[2:]
print(oldest, second_oldest)
print(others)

# catch-all
# 先頭2つと記述しなくてもその他を取得することができる！
# 固定値を記入する必要がないため、変更しやすくバグを生みにくい(特にoff-by-one)
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest)
print(others)

# 置き方も多様
*a, b, c = car_ages
print(a, b, c)
a, *b, c = car_ages
print(a, b, c)
a, b, *c = car_ages
print(a, b, c)



