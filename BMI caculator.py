# BMI calculator

name = raw_input("Please enter your name: ")
height_m = input("Please enter your height in meter: ")
weight_kg = input("Please enter your weight in kg: ")

def bmi_caculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweigth"
    else:
        return name + " is overweight"

result = bmi_caculator(name, height_m, weight_kg)

print(result)
