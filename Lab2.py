def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi= weight/pow(height,2)
 print("BMI =" + str(bmi))
 if(bmi<18.5):
     print("You are underweight")
 elif(bmi<=25):
     print("You are normal weight")
 elif(bmi>25):
     print("You are overweight")

calculate_bmi(weight=18.4, height=1)