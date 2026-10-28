def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        weight_classification = "Underweight"
    elif 18.5 <= bmi <= 25:
        weight_classification = "Normal Weight"
    else: 
        weight_classification = "Overweight"

    print(f"Weight Classification = {weight_classification}")


calculate_bmi(weight=57, height=1.73)