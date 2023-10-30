def calc_average(list):
 total=0
 for i in range(len(list)):
  total+=list[i]
 avg=total/len(list)
 return avg

def get_user_input():
 numbers=input()
 numberlist=numbers.split(",")
 for i in range(len(numberlist)):
  numberlist[i]=float(numberlist[i])
 return numberlist

def find_min_max(list):
 min=list[0]
 max=0
 for i in range(len(list)):
  if (list[i]<min):
   min=list[i]
  if(list[i]>max):
   max=list[i]
 minmaxlist=[min,max]
 return minmaxlist

def sort_temperature(list):
 list.sort()
 return list

def calc_median_temperature(list):
 a = float(len(list))

 if a % 2 == 0:
  b = float(list[len(list) // 2])
  c = float(list[(len(list) // 2) - 1])
  d = (b + c) / 2.0
  return float(d)

 if a % 2 > 0:
  return float(list[len(list) // 2])


def display_main_menu():
 print("Enter some numbers separated by commas (e.g. 5, 67,32)")
 return
def main():
 print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
 display_main_menu()
 num_list = get_user_input()

 print("Average= " +str(calc_average(num_list)))
 print("MinMax= " +str(find_min_max(num_list)))
 print("Median= " +str(calc_median_temperature(sort_temperature(num_list))))

if __name__ == "__main__":
     main()