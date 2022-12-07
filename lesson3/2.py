print("Ваши координаты 0:0, Введите куда будем двигаться(целые числа)?")
x = 0
y = 0
stop_word = 'ДА'
while stop_word == 'ДА':
  xr = int(input('Вправо на:'))
  xl = int(input('Влево на:'))
  yu = int(input('Вверх на:'))
  yd = int(input('Вниз на:'))
  x += xr - xl
  y += yu - yd
  print("Текущие координаты:", x,y)
  stop_word = input('Продолжим? (Да/Нет):').upper()
  while stop_word != 'ДА' and stop_word != 'НЕТ':
    stop_word = input('Продолжим? (Да/Нет):').upper()