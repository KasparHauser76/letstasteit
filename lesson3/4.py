import math
a = complex((input("Введите значение a= ")))
b = complex((input("Введите значение b= ")))
c = complex((input("Введите значение c= ")))
discr = b ** 2 - 4 * a * c
if discr != 0:
    sd=discr**0.5
    x1 = ( -b + sd)/(2*a)
    x2 = ( -b - sd)/(2*a)
    print('D=',sd, '\n', 'x1',x1, 'x2',x2)
else:
    x = -b/(2*a)
    print('D=0', '\n', 'x',x)