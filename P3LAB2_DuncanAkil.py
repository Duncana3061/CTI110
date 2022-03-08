service = input("Enter desired auto service:\n")
print("You entered: " +service)

if service.lower() == "oil change":

   print("Cost of oil change: $35")

elif service.lower() == "car wash":

   print("Cost of car wash: $7")

elif service.lower() == "tire rotation":

   print("Cost of tire rotation: $19")

else:

   print("Error: Requested service is not recognized")