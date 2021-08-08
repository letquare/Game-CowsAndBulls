from game_engine import GameEngine


def game_bulls_and_cows():

    """

    Правила:
        # Компьютер загадывает четырехзначное число, все цифры которого различны
        # (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
        # Игрок вводит четырехзначное число c неповторяющимися цифрами,
        # компьютер сообщают о количестве «быков» и «коров» в названном числе
        # «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
        #       что и в задуманном числе
        # «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
        #       что и в задуманном числе
        #
        # Например, если задумано число 3275 и названо число 1234,
        # получаем в названном числе одного «быка» и одну «корову».
        # Очевидно, что число отгадано в том случае, если имеем 4 «быка».
    """

    engine = GameEngine()
    rulls = input('Тебе рассказать правила [y/n] ')
    if rulls == 'y':
        print(game_bulls_and_cows.__doc__)
    engine.guess_number()
    print('Тебе нужно ввести 4х значное число, без 0 на первой позиции и не повторяй числа')
    count = 0
    while True:
        try:
            user_input = int(input('Какое я загадал число? '))
            error = engine.check_number(number=user_input)
            if error:
                print(error)
                continue
            animals = engine.animal_counter()
            print(f'cows = {animals[0]}')
            print(f'bulls = {animals[1]}')
            if animals[1] == 4:
                engine.my_clear()
                break
            count += 1
        except ValueError:
            print('Только цифры ')
    print('Ты угадал(а)!Поздравляю!/Congratulation!')
    print(f'На это тебе потребовалось {count} попыток')


print('Привет! Я - Марк! Сыграем в игру "Быки и коровы"?')

game_bulls_and_cows()

while True:
    user = input('Сыграем еще? [y/n]')
    if user == 'y':
        game_bulls_and_cows()
    else:
        exit('Спасибо, что поиграл(a) со мной! Пока!')
