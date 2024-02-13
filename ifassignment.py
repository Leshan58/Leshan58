weight =int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif 18.5 > bmi < 25:
    print("normal")
elif 25 > bmi <30:
    print("overweight")
else:
    print("obese")

