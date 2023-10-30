def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi= weight/pow(height,2)
 print("BMI =" + str(bmi))
 if(bmi<18.5):
     print("You are underweight")
     return -1
 elif(bmi<=25):
     print("You are normal weight")
     return 0
 elif(bmi>25):
     print("You are overweight")
     return 1


def main():
    return_value= calculate_bmi(1.6,49)
    print(return_value)
if __name__ == "__main__":
     main()