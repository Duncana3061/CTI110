# Calculating the total purchases
# Feb 25 2022
# CTI-110 P2HW1 - Total Purchases
# Akil Duncan
#


#declare variable for price of items
item1 = float(input("Enter the price of item #1: "))
item2 = float(input("Enter the price of item #2: "))
item3 = float(input("Enter the price of item #3: "))
item4 = float(input("Enter the price of item #4: "))
item5 = float(input("Enter the price of item #5: "))

#declare variable for subtotal of items
stotal = item1 + item2 + item3 + item4 + item5

#declare variable for sales tax
tax = stotal * 0.07

#declare variable for total amount
total = stotal + tax

#display results
print('----Results----')

#display subtotal
print('Subtotal: ', stotal)

#display sales tax
print('Sales Tax: ', round(tax, 2))

#display overall total
print('Total: ', round(total, 2))


