weight = float(input('Enter your weight in kilograms : '))
height = float(input('Enter your height in metres : '))
bmi = weight / height ** 2
print('Your BMI is ' , format(bmi , '.2f'))