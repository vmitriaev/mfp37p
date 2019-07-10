# calc v1

what = input("Выберите действие (+, -, *, /): ")

a = int(input("Первое число: "))
b = int(input("Второе число: "))

if what == "+":
    c = a + b
    print("Результат: " + str(c))

elif what == "-":
    c = a - b
    print("Результат: " + str(c))

elif what == "*":
    c = a * b
    print("Результат: " + str(c))

elif what == "/":
    c = a / b
    print("Результат: " + str(c))

else:
    print("Выбрана неверная операция!")
