f1 = 1
f2 = 1

n = int(input("Введите номер числа Фиббоначи:"))

a = 0
while a < n - 2:
    fs = f1 + f2
    f1 = f2
    f2 = fs
    a = a + 1

print(f"Значение {n}-го числа:", f2)