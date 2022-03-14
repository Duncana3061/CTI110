# CTI-110
# P3HW2 - Pizza Order
# Akil Duncan
# March 11 2022
#


#declare variable for number of students
students = int(input("How many students do you want to order pizza for? "))

#declare variable for number of people
people = float(input("Enter number of people per pizza (1.5, 2 or 3): "))

#declare variable for number of slices per student
slices = students * 3

#declare variable for number of pizzas
pizzas = slices / 6

#declare variable for total amount 
total = pizzas * 5.00

#declare variable for tax
tax = 0.06 * total

#declare variable for price
price = total + tax


#display results
if people == 1.5 or 2 or 3:
    print("----Pizza Order----")
    print("Number of Students : ", students)
    print("Pizzas Needed: ", round(pizzas))
    print("Price: $", round(price,2))    

elif people != 1.5 or 2 or 3:
    print("INVALID ENTRY!!!!")
    print("Should have entered 1.5, 2 or 3")
    print("Run program again")


   

