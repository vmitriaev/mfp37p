# here about "if"

number = 42
guess = int(input("Угадай какое целое число я загадал? Напечатай, затем нажми Enter: "))

if guess == number:
    print("Поздравляю, число угадано!")

elif guess < number:
    print("К сожалению, загаданное число больше чем " + str(guess))

else:
    print("К сожалению, загаданное число меньше чем " + str(guess))
