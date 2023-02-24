# for i in range(1, 10, 1):
#     print('3','*', i ,'=', (i * 3))

# ls = list(range(1, 101))
# print(ls)
# a = sum(ls)
# print(a)
# b = len(ls)
# print(b)
# result = a/b
# print(result)

def func(number:int):
    count=0
    if number < 50:
        return 'Ви ввели надто маленьке число'
    else:
        while number > 50:
            number/= 2
            count += 1
        return f'Число яке вийшло {number} та число ітерацій {count}'

print(func(45))
print(func(1000))










