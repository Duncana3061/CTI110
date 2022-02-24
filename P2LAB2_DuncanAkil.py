current_price = int(input())
last_months_price = int(input())
mortgage = (current_price * 0.051) / 12
change = current_price - last_months_price


print('This house is $'f'{current_price}.'' The change is $'f'{change}'' since last month.')
print('The estimated monthly mortgage is $'f'{mortgage:.2f}.')
   