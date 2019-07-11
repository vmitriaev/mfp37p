# here about "continue"

while True:
    s = input("Введи что угодно (exit для завершения): ")

    if s == "exit":
        break

    if len(s) < 3:
        print("Недостаточная длина строки!")
        continue

    print("Длина строки оптимальна!")
