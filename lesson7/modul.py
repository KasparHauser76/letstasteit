import time


def wait():
    """Бесполезно тратит 5 секунд жизни"""
    print('Отсчёт пошёл')
    time.sleep(5)
    print('Прошло 5 секунд')


wait()

def summary(x, y):
    """Очень даже полезно складывает два целых числа"""
    return x + y
print(summary(2, 4))