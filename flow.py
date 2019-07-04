import calendar

print("Now you will know at what weekday was your birthday")

y = input("Enter year of your birthday: ")
m = input("Enter month of your birthday: ")
d = input("Enter day of your birthday: ")

calcdate = calendar.weekday(int(y), int(m), int(d))

if calcdate == 1:
    print("The weekday of your birthday is monday!")

elif calcdate == 2:
    print("The weekday of your birthday is tuesday!")

elif calcdate == 3:
    print("The weekday of your birthday is wednesday!")

elif calcdate == 4:
    print("The weekday of your birthday is thursday!")

elif calcdate == 5:
    print("The weekday of your birthday is friday!")

elif calcdate == 6:
    print("The weekday of your birthday is saturday!")

elif calcdate == 7:
    print("The weekday of your birthday is sunday!")

else:
    print("Something goes wrong")
