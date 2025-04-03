temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print("It's hot")
    print("It's sunny")
elif temp < 0 and is_sunny:
    print("It's cold")
    print("It's sunny")
elif temp >0 and is_sunny:
    print("It's warm")
    print("It's sunny")
if temp >= 28 and not is_sunny:
    print("It's hot")
    print("It's cloudy")
elif temp < 0 and not is_sunny:
    print("It's cold")
    print("It's cloudy")
elif temp >0 and not is_sunny:
    print("It's warm")
    print("It's cloudy")