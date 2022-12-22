while True:
    try:
        n = int(input('Номер элемента ряда Фибоначчи(рекурсия):  '))
        def fibonacci(n):
            """вернёт заданное число Фиббоначи, через рекурсию"""
            if n in (1, 2):
                return 1
            return fibonacci(n - 1) + fibonacci(n - 2)
        print(fibonacci(n))
    except:
        print('только натуральное число')

    x = input('продолжим? (да/нет) ')
    if x == 'нет':
        break
    while x != 'да':
        x = input('Продолжим? (да/нет) ')