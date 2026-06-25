#BMI CALCULATOR
name=input("enter your name=")
age=int(input("enter your age="))
height=float(input("enter your height in meters="))
weight=int(input("enter your weight in kilograms="))
bmi=weight/height**2
print("your bmi is=",bmi)
if(bmi<18):
    print("you are underweight")
elif(bmi>25):
    print("you are overweigth")
else:
    print(f"{name},you are healthy")