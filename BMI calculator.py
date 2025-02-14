#BMI TRACKER
# BMI = [weight (kg) / height (cm) / height (cm)] x 10,000
def bmicalculator ():
    
    print ("Hello! Welcome to the BMI Calculator")
    weight =  input ('What is your Weight (Kg) ')
    while weight == "":
        print('Please Enter your weight')
        weight = input ('What is your Weight (Kg) ') 
        
    height = input ('What is your height(cm) ')
    while height == "":
        print(' Please Enter your Height')
        height = input ('What is your Height (cm) ')
    
    Weight = float(weight)
    Height = float (height)
    Bmi =  Weight / (Height * Height) * 10000
    if Bmi < 18.5:
        print(f'Your BMI is {Bmi}, You are underweight')
    elif 18.5 <= Bmi < 25:
        print(f'Your BMI is {Bmi}, You are normal weight')
    elif 25 <= Bmi < 30:
        print(f'Your BMI is {Bmi}, You are overweight')
    else:
        print(f'Your BMI is {Bmi}, You are obese')
            
    
    
bmicalculator()