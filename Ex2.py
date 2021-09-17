year = int(input("Введите год: "))

if year % 400 == 0:
    print("%d високосный" %year)
elif year % 100 == 0:
    print("%d не високосный" %year)
elif year % 4 == 0:
    print("%d високосный" %year)
else:
    print("%d не високосный" %year)