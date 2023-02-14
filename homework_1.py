# Task 1
#
# age = int(input("Enter your age: "))
# if age < 0:
#     print ("Невірний вік")
# elif age >=0 and age < 18:
#     print ("Ви ще неповнолітній")
# else:
#     print ("Ви стали дорослим")
#
# Task 2
#
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# if a % b == 0:
#     print("Ділиться")
#     print(round(a / b))
# elif a % b != 0:
#     print("Ділиться з залишком:")
#     print(a % b)
#
# Task 3
#
years = int(input("Введите стаж:"))
zp = float(input("Введите зарплату:"))
if years >= 1 and years < 3:
    result = zp / 100 * 10 + zp
    print(result)
elif years >= 3:
    result = (zp / 100 * 20 + zp)
    print(result)
if result < 4000:
    bonus = result + 1000
    print(bonus)
else:
    bonus = result + 500
    print(bonus)





