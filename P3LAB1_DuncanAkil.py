red = int(input())
green = int(input())
blue = int(input())

num1 = (red, green, blue)
small = min(num1) 

gred = (red - small) 
ggreen = (green - small)
gblue = (blue - small)

print(gred, ggreen, gblue)
