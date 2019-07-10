# here about "break"

while True:
    s = input("Введи что угодно, а я посчитаю длину строки. Для завершения введи exit: ")

    if s == "exit":
        break

    print("Длина строки: ", len(s))

print("Завершение")
