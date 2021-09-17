print("Четное число или нечетное\n")
num = int(input("Введите число: "))
if num % 2 == 0:
    print(num, " - четное число")
elif num % 2 == 1:
    print(num, " - нечетное число")
else:
    print("Это не число!")