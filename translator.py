rutranslate={
    'The Cities Game': 'Игра в Города',
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
    'Enter to exit: ': 'Введите для выхода: '
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