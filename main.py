length = float(input("The length of a zander in centimeters:"))
if length < 42:
    limit = 42 - length
    print("Release the fish back into the lake.")
    print("The caught fish was", limit, "centimeters below the size limit ")
else:
    print("The zander fulfills the size limit")


cabin = str(input("Enter the cabin class of a cruise ship:"))
if cabin == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin=="A":
    print("A: above the car deck, equipped with a window.")
elif cabin == "B":
    print("B: windowless cabin above the car deck.")
elif cabin == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class")


gender = str(input("Your biological gender:"))
value = float(input("Your hemoglobin value (g/l):"))
if gender == "female":
  if value < 117:
   print("The hemoglobin value is low.")
  elif value > 155:
   print("The hemoglobin value is high.")
  else:
    print("The hemoglobin value is normal.")
if gender == "male":
  if value < 134:
    print("The hemoglobin value is low.")
  elif value > 167:
    print("The hemoglobin value is high.")
  else:
    print("The hemoglobin value is normal.")


year = int(input("Enter a year:"))
if year%4==0:
  print(str(year)+" is a leap year.")
elif year%100==0 and year%400==0:
  print(str(year)+" is a leap year.")
else:
  print(str(year)+" is NOT a leap year.")




