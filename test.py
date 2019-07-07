def bmi_status(mass, height):
    """For adults only. Mass should be in kilograms and height in metres."""
    bmi = mass / (height ** 2)
    print("Body mass index is {0:.1f}".format(bmi))
    
    if bmi < 25:
        status = "NORMAL"
    elif bmi < 29:
        status = "OVERWEIGHT"
    else:
        status = "OBESE"
    return status
    
print("Your BMI indicates that you are {0} for your height and weight".format(bmi_status(80, 1.8)))
print("---------")
print("Your BMI indicates that you are {0} for your heigh and weightt".format(bmi_status(90, 1.8)))
print("---------")
print("Your BMI indicates that you are {0} for your height and weight".format(bmi_status(100, 1.8)))