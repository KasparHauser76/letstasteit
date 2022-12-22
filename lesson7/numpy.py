import numpy as np

array = np.random.randint(1,100, size=(3,3))
array_transpose = np.transpose(array)
print("Массив со случайнами числами: ", array)
print("Транспонированный массив: ", array_transpose)