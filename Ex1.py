print("Even or not\n")
num = int(input("Put your number: "))
if num == 0:
    print(num, " - this is ZERO")
elif num % 2 == 0:
    print(num, " - even number")
elif num % 2 == 1:
    print(num, " - uneven number")
else:
    print("It's not a number!")
