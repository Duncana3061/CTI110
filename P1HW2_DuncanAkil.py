# Calculating the number of pizza and slices per student
# Feb 14 2022
# CTI-110 P1HW2 - Pizza Order
# Akil Duncan
#

#declare variable for number of students
students = int(input("Enter the number of students: "))

#declare variable for number of slices per student
slices = students * 3

#display number of slices per student
print('Number of slices needed: ', slices)

#delclare variable for number of pizzas
pizzas = slices / 6

#display number of pizzas needed
print('Number of pizzas needed: ', pizzas)
