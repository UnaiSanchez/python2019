def add(amount):
    def func(value):
        return value +amount
    return func
add_5=add(5)
add_10=add(10)
add_1000=add(1000)
print(add_1000(10))


