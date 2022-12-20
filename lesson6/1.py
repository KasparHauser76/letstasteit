def coding():
    x = ['т', 'е', 'с', 'n', '1']
    y = ''
    print('Список строк: ', x)
    for i in x:
        y += i
    print('Закодированная последовательность:', y.encode('utf-8'))

coding()

def decoding():
    c = b'\xd1\x82\xd0\xb5\xd1\x81\xd1\x82\x31'.decode('utf-8')
    print('Декодированная последовательность:', c)

decoding()