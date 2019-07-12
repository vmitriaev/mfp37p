# here about "list" (список)

shoplist = ["apple", "mango", "banana"]

print("I need to buy " + str(len(shoplist))` + " items.")

print("Items: ", end=" ")

for item in shoplist:
    print(item, end=" ")

print("\nAlso, i need buy rise too.")

shoplist.append("rise")

print("Let's sort my list!")

shoplist.sort()

print("Here is my sorted list: " + shoplist)

print("At first I need to buy", shoplist[0])

olditem = shoplist[0]

del shoplist[0]

print("I buy ", olditem)

print("Here is my actual list: ", shoplist)
