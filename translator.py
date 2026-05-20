rutranslate={
    'The Cities Game 🏙️': 'Игра в Города',
    'Enter the word: ': 'Введите слово: ',
    'Error!!!': 'Ошибка!!!',
    'Game Over!!!': 'Игра окончена!!!',
    'You win!!!': 'Вы победили!!!',
    'This word has already been used.': 'Это слово уже было использовано.',
    'You have': 'У вас есть',
    'hearts. Enter the word: ': 'сердец. Введите слово: ',
    'You received': 'Вы получили',
    'points.': 'баллов.',
    'Absolute Champion!!! 🏆': 'Абсолютный чемпион!!! 🏆',
    'Loser!!!': 'Неудачник!!!',
    'Creator: Abdyrahym Begenjov': 'Создатель: Абдырахым Бегенджов',
    'Enter to start game: ': 'Нажмите, чтобы начать игру: ',
    'Loading...': 'Загрузка...',
    'You must enter the word!!!': 'Вы должны ввести слово!!!',
    'Enter to exit: ': 'Введите для выхода: ',
    'Enter your name: ': 'Введите свое имя: ',
    'Enter to exit mode: ': 'Войдите в режим выхода: ',
    'Game      Rules      Records      Settings      Exit': 'Игра      Правилы      Рекорды      Настройки      Выход',
    'Choose a game mode: ': 'Выберите режим игры: ',
    'Do you want to change parameters (Enter \"Name\" or \"Language\"): ': 'Хотите ли вы изменить параметры (введите \"Имя\" или \"Язык\"): ',
    'Do you want to exit: ': 'Вы хотите выйти: ',
    'Goodbye!!!': 'До свидания!!',
    'Name': 'Имя',
    'Language': 'Язык',
    'Return': 'Вернуться',
    'Game': 'Игра',
    'Rules': 'Правилы',
    'Records': 'Рекорды',
    'Settings': 'Настройки',
    'Exit': 'Выход',
    'LEADERBOARD': 'ЛИДЕРБОРД'
             }


entranslate={j: i for i, j in rutranslate.items()}


def translator(word, language):
    match language:
        case 'en':
            return word
        case 'en1':
            if word not in entranslate:
                return 'Error!!!'
            return entranslate[word]
        case 'ru':
            return rutranslate[word]
        case _:
            return '???'