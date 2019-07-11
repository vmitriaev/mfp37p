# here about "def" (functions) and "return"

def maximum(x, y):
    if x > y:
        return x

    elif x == y:
        return "Числа равны"

    else:
        return y


a = input("Введи целое число: ")

b = input("Введи второе: ")

print(maximum(a, b))
