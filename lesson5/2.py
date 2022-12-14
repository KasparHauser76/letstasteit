def password():
    p = input("Введите пароль: ")
    if len(p) < 6:
        print('Должен быть не менее 6 знаков')
        return False
    elif "".join(p).lower() == 'password' or "".join(p).upper() == 'PASSWORD':
        print('Слишком просто, напрягись')
        return False
    elif not any(p1.isdigit() for p1 in p):
        print('должен содержать хотя бы одну цифру')
        return False
    elif all(p2.isdigit() for p2 in p):
        print('не должен состоять только из цифр')
        return False
    else:
        print('Хороший пароль')
        return True

password()