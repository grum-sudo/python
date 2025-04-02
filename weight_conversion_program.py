weight = float(input("Enter weight: "))
unit = input("Enter unit (k/l): ").lower()
if unit == "k": 
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Weight is: {round(weight, 2)}")
elif unit == "l":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Weight is: {round(weight, 2)}")
else: 
    print(f"{unit} is not a valid unit")
