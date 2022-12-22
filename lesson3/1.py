# движение по кооржинатам x, y, вправо, влево, вверх и вниз.

print("Your position 0:0. Pleace, enter where you want to go(integer):")
x = 0
y = 0
xr = int(input('Right on:'))
xl = int(input('Left on:'))
yu = int(input('Up on:'))
yd = int(input('Down on:'))
print("Your new coordinates is:", x + xr - xl, y+yu-yd)