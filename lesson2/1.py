# для того, чтобы не забыть через пол года,
# данный код выполняет логарифмические действия
# с вводимыми пользователем числами

num1 = float(input('Pleace input some number50: '))
num2 = float(input('Pleace input another some number: '))

sum = num1+num2
addition = 'addition %s'
print(addition % sum)

sub = num1-num2
subtraction = 'subtraction %s'
print(subtraction % sub)

mul = num1*num2
multiplication = 'multiplication %s'
print(multiplication % mul)

div = num1/num2
division = 'division %s'
print(division % div)

exp = num1**num2
exponentiation = 'exponentiation %s'
print(exponentiation % exp)

mod = num1%num2
modulo = 'modulo %s'
print(modulo % mod)

intdev = num1//num2
integer_division = 'integer division %s'
print(integer_division % intdev)