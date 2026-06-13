rutranslate={
    'The Cities Game 🏙️': 'Игра в Города',
    'Enter the word: ': 'Введите слово: ',
    'Error!!!': 'Ошибка!!!',
    'Game Over!!!': 'Игра окончена!!!',
    'You win!!!': 'Вы победили!!!',
    'This word has already been used.': 'Это слово уже было использовано.',
    'You have': 'У вас есть',
    '❤️. Enter the word: ': '❤️. Введите слово: ',
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
    'Game      Rules      Highscores      Settings      Exit': 'Игра      Правилы      Рекорды      Настройки      Выход',
    'Choose a game mode: ': 'Выберите режим игры: ',
    'Do you want to change parameters (Enter \"Name\" or \"Language\"): ': 'Хотите ли вы изменить параметры (введите \"Имя\" или \"Язык\"): ',
    'Do you want to exit (\"Yes\" or \"No\"): ': 'Вы хотите завершить (\"Да\" или \"Нет\"): ',
    'Goodbye!!!': 'До свидания!!',
    'Name': 'Имя',
    'Language': 'Язык',
    'No': 'Нет',
    'Game': 'Игра',
    'Rules': 'Правилы',
    'Highscores': 'Рекорды',
    'Settings': 'Настройки',
    'Exit': 'Выход',
    'NAME |': 'ИМЯ |',
    'POINTS': 'БАЛЛЫ',
    'LEADERBOARD:': 'ЛИДЕРБОРД:',
    'You are ABSOLUTE CHAMPION!!!': 'Вы АБСОЛЮТНЫЙ ЧЕМПИОН!!!',
    'You\'ve broken a new highscore!!!': 'Вы побили новый рекорд!!!'
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