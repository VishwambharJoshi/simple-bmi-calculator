
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi =  round (weight / height ** 2)
#print (round(bmi, 2))

if bmi < 18.5:
  print(f"Your bmi is {bmi}, Your are underweight")
elif bmi < 25:
  print(f"Your bmi is {bmi}, Your are normal weight")
elif bmi <30:
  print(f"Your bmi is {bmi}, Your are over weight")
elif bmi<35:
  print(f"Your bmi is {bmi}, Your are obese")
else:
  print(f"Your bmi is {bmi}, Your are clinically obese")
