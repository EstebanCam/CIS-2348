'''
Esteban Camarillo
ID number: 1636095
Lab: 2.19
'''
lemon_juice = float(input("Enter amount of lemon juice (in cups):"))
water = float(input("Enter amount of water (in cups):"))
agave_n = float(input("Enter amount of agave nectar (in cups):"))
servings = float(input("How many servings does this make?"))

size = input("Lemonade ingredients - yields 6.00 servings")
print('{:.2f}'.format(lemon_juice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave_n), "cup(s) agave nectar")

make = float(input("How many servings would you like to make?"))
lemon_juice = float((1/3) * make)
water = float((2+(2/3)) * make)
agave_n = float((2.50/6) * make)

print(lemon_juice, "cup(s) lemon juice")
print(water, "cup(s) water")
print(agave_n, "cup(s) agave nectar")

convert = input("Lemonade ingredients - yields 48.00 servings")
lemon_juice = (lemon_juice * 0.0625)
water = (water * 0.0625)
agave_n = (agave_n * 0.0625)
