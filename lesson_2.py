# calc v2: color
#
from colorama import Fore, Back
from colorama import init

# use Colorama to make Termcolor work on Windows too
init()

print(Fore.BLACK)

print(Back.GREEN)

what = input("Выберите действие (+, -, *, /): ")

print(Back.CYAN)

a = int(input("Первое число: "))
b = int(input("Второе число: "))

print(Back.YELLOW)

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
