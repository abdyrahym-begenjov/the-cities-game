from propython import *
from translator import *
from subprocess import run
from platform import system

def clear_screen():
    current_os=system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def enter_lang(data):
    print('English |  Русский')
    while True:
        chosen_language=input()
        chosen_language=chosen_language.title().strip()
        match chosen_language:
            case 'Русский':
                lang='ru'
                cities_list=pyread('goroda.json')
                break
            case 'English':
                lang='en'
                cities_list=pyread('cities.json')
                break
            case _:
                continue
    
    data['language']=lang
    data['cities']=cities_list
    pywrite('data.json', data)
    return lang, cities_list

def enter_name(data, lang):
    while True:
        name=input(translator('Enter your name: ', lang))
        if name!='':
            data['name']=name
            pywrite('data.json', data)
            return name
        
def star(points, lang):
    match points:
        case n if n>=60:
            return translator('Absolute Champion!!! 🏆', lang)
        case n if n>=50:
            return '⭐⭐⭐⭐⭐'
        case n if n>=40:
            return '⭐⭐⭐⭐'
        case n if n>=30:
            return '⭐⭐⭐'
        case n if n>=20:
            return '⭐⭐'
        case n if n>=10:
            return '⭐'
        case _:
            return translator('Loser!!!', lang)

def leaderboard(base, lang):
    print(translator('LEADERBOARD:', lang))
    base=dict(sorted(base.items(), key=lambda x: x[1], reverse=True))
    for i, j in base.items():
        print(f'{i}: {j}')

def new_word(word, lang):
    word=word.strip().title()
    if lang=='ru':
        word=translator(word, 'en1')
    return word