#Write a program to calculate the BMI of a person?
w=int(input("Write you weight in kilograms"))
h=int(input("Write your height in meters"))
BMI=w/(h**2)
if BMI<18.5:
    print("underweight")
elif BMI>18.5 and BMI<24.9:
    print("healty")
elif BMI>25 and BMI<29.9:
    print("obese")
else:
    print("severly obese")