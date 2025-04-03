temp = -5
is_sunny = True

if temp >= 28 and is_sunny:
    print("It's hot")
    print("It's sunny" if is_sunny else "It's not sunny")
elif temp < 0 and is_sunny:
    print("It's cold")
    print("It's sunny" if is_sunny else "It's not sunny")
elif temp >0 and is_sunny:
    print("It's warm")
    print("It's sunny")