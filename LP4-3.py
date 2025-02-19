egg_amount = int(input("HOW MANY EGSS: "))
egg_left = egg_amount % 12
total_price = 0
price_per = 0

def eggs():
    if 4 > egg_amount > 0:
        price_per = 0.50
    if 6 > egg_amount > 3:
        price_per = 0.45