from random import choice
from propython import pyread, pywrite
from time import sleep
from translator import *
from subprocess import run
import platform

base=pyread('base.json')
data=pyread('data.json')

def clear_screen():
    current_os=platform.system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def enter_name():
    while True:
        name=input(translator('Enter your name: ', lang))
        if name!='':
            data['name']=name
            pywrite('data.json', data)
            return name

def enter_lang():
    print('English |  Русский')
    while True:
        chosen_language=input()
        chosen_language=chosen_language.title().strip()
        if chosen_language=='English' or chosen_language=='Русский':
            break

    match chosen_language:
        case 'Русский':
            lang='ru'
            cities_list=pyread('goroda.json')
        case 'English':
            lang='en'
            cities_list=pyread('cities.json')
    data['language']=lang
    data['cities']=cities_list
    pywrite('data.json', data)
    return lang, cities_list

name=data['name']
lang=data['language']
cities_list=data['cities']

if lang=='' and cities_list=='':
    lang, cities_list=enter_lang()

if name=='':
    name=enter_name()

while True:
    print(translator('The Cities Game 🏙️', lang))
    print(f'{translator('Creator: Abdyrahym Begenjov', lang)}     (GitHub: abdyrahym-begenjov)')
    print(translator('Game      Rules      Records      Settings      Exit', lang))
    mode=input(translator('Choose a game mode: ', lang))
    mode=mode.title().strip()
    if lang=='ru':
        mode=translator(mode, 'en1')
    match mode:
        case 'Game':
            start=input(translator('Enter to start game: ', lang))
            print(translator('Loading...', lang))
            sleep(2)

            word=choice(cities_list)
            hearts=3
            points=0
            number=1
            cities_set=set()

            print(f'{number}) {word}')

            while True:
                if word[-1] in ('ъ', 'ы', 'ь'):
                    word=word[:-1]
                city=word
                if hearts!=0:
                    word=input(f'{translator('You have', lang)} {hearts} {translator('❤️. Enter the word: ', lang)}')
                    word=word.title().strip()
                if hearts==0:
                    print(translator('Game Over!!!', lang))
                    print(f'{translator('You received', lang)} {points} {translator('points.', lang)}')
                    match points:
                        case n if n>=60:
                            print(translator('Absolute Champion!!! 🏆', lang))
                        case n if n>=50:
                            print('⭐⭐⭐⭐⭐')
                        case n if n>=40:
                            print('⭐⭐⭐⭐')
                        case n if n>=30:
                            print('⭐⭐⭐')
                        case n if n>=20:
                            print('⭐⭐')
                        case n if n>=10:
                            print('⭐')
                        case _:
                            print(translator('Loser!!!', lang))
                    break
                elif word=='':
                    print(translator('You must enter the word!!!', lang))
                    print(translator('Error!!!', lang))
                    hearts-=1
                    word=city
                elif word[0]==city[-1].upper() and word in cities_list and word not in cities_set:
                    number+=1
                    print(f'{number}) {word}')
                    points+=1
                    cities_set.add(word)
                else:
                    if word in cities_set:
                        print(translator('This word has already been used.', lang))
                    print(translator('Error!!!', lang))
                    hearts-=1
                    word=city
            
            if name not in base:
                base[name]=points
                pywrite('base.json', base)
            if base[name]<points:
                base[name]=points
                pywrite('base.json', base)
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()
        case 'Rules':
            if lang=='ru':
                rules=pyread('ru_rules.txt')
            else:
                rules=pyread('en_rules.txt')
            print(rules)
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()
        case 'Records':
            print(translator('LEADERBOARD:', lang))
            base=dict(sorted(base.items(), key=lambda x: x[1], reverse=True))
            for i, j in base.items():
                print(f'{i}: {j}')
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()
        case 'Settings':
            while True:
                print(f'{translator('Name', lang)}: {data['name']}')
                print(f'{translator('Language', lang)}: {data['language']}')
                change=input(translator('Do you want to change parameters (Enter \"Name\" or \"Language\"): ', lang))
                change=change.title().strip()
                if lang=='ru':
                    change=translator(change, 'en1')
                match change:
                    case 'Name':
                        name=enter_name()
                        clear_screen()
                    case 'Language':
                        lang, cities_list=enter_lang()
                        clear_screen()
                    case _:
                        break
            clear_screen()

        case 'Exit':
            exit_confirm=input(translator('Do you want to exit: ', lang))
            exit_confirm=exit_confirm.title().strip()
            if lang=='ru':
                exit_confirm=translator(exit_confirm, 'en1')
            if exit_confirm=='Return':
                clear_screen()
            else:
                print(translator('Goodbye!!!', lang))
                input(translator('Enter to exit: ', lang))
                break
        case _:
            clear_screen()