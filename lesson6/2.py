import io
import math

# считаем максимально возможное число молекул пирта, 
# забирая значения из файла Input.txt

with io.open('/home/kaspar/tensor/lesson6/Input.txt', encoding='utf-8') as f:
        a = f.read().split()
print('Начальные значения:', a)
C = math.floor(int(a[0])/2)
H = math.floor(int(a[1])/6)
O = math.floor(int(a[2])/1)
print('Максимально возможно число молекул спирта: ', min(C, H, O))