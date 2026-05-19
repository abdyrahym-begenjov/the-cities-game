from random import choice
from propython import pyread, pywrite
from time import sleep
from translator import *
from os import system

base=pyread('base.json')
data=pyread('data.json')

def enter_name():
    while True:
        name=input(translator('Enter your name: ', lan))
        if name!='':
            data['name']=name
            pywrite('data.json', data)
            return name

def enter_lan():
    print('English |  Русский')
    while True:
        choose_language=input()
        choose_language=choose_language.title().strip()
        if choose_language=='English' or choose_language=='Русский':
            break

    match choose_language:
        case 'Русский':
            lan='ru'
            cities_list=pyread('goroda.json')
        case 'English':
            lan='en'
            cities_list=pyread('cities.json')
    data['language']=lan
    data['cities']=cities_list
    pywrite('data.json', data)
    return lan, cities_list

name=data['name']
lan=data['language']
cities_list=data['cities']

if lan=='' and cities_list=='':
    lan, cities_list=enter_lan()

if name=='':
    name=enter_name()

while True:
    print(translator('The Cities Game', lan))
    print(f'{translator('Creator: Abdyrahym Begenjov', lan)}     (GitHub: abdyrahym-begenjov)')
    print(translator('Game      Records      Settings      Exit', lan))
    mode=input(translator('Choose the mode of game: ', lan))
    mode=mode.title().strip()
    if lan=='ru':
        mode=translator(mode, 'en1')
    match mode:
        case 'Game':
            start=input(translator('Enter to start game: ', lan))
            print(translator('Loading...', lan))
            sleep(2)

            word=choice(cities_list)
            heart=3
            points=0
            number=1
            cities_set=set()

            print(f'{number}) {word}')

            while True:
                if word[-1] in ('ъ', 'ы', 'ь'):
                    word=word[:-1]
                city=word
                if heart!=0:
                    word=input(f'{translator('You have', lan)} {heart} {translator('hearts. Enter the word: ', lan)}')
                    word=word.title().strip()
                if heart==0:
                    print(translator('Game Over!!!', lan))
                    print(f'{translator('You received', lan)} {points} {translator('points.', lan)}')
                    match points:
                        case n if n>=60:
                            print(translator('Absolute Champion!!! 🏆', lan))
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
                            print(translator('Loser!!!', lan))
                    break
                elif word=='':
                    print(translator('You must enter the word!!!', lan))
                    print(translator('Error!!!', lan))
                    heart-=1
                    word=city
                elif word[0]==city[-1].upper() and word in cities_list and word not in cities_set:
                    number+=1
                    print(f'{number}) {word}')
                    points+=1
                    cities_set.add(word)
                else:
                    if word in cities_set:
                        print(translator('This word has already been used.', lan))
                    print(translator('Error!!!', lan))
                    print(word)
                    heart-=1
                    word=city
            
            if name not in base:
                base[name]=points
                pywrite('base.json', base)
            if base[name]<points:
                base[name]=points
                pywrite('base.json', base)
            end=input(translator('Enter to exit mode: ', lan))
            system('cls')
        case 'Records':
            base=dict(sorted(base.items(), key=lambda x: x[1], reverse=True))
            for i, j in base.items():
                print(f'{i}: {j}')
            end=input(translator('Enter to exit mode: ', lan))
            system('cls')
        case 'Settings':
            while True:
                print(f'{translator('Name:', lan)} {data['name']}')
                print(f'{translator('Language:', lan)} {data['language']}')
                change=input(translator('Do you want to change parametrs (Enter \"Name\" or \"Language\"): ', lan))
                change=change.title().strip()
                if lan=='ru':
                    change=translator(change, 'en1')
                match change:
                    case 'Name':
                        name=enter_name()
                        system('cls')
                    case 'Language':
                        lan=enter_lan()
                        system('cls')
                    case _:
                        break
            system('cls')

        case 'Exit':
            exit=input(translator('Do you want to exit: ', lan))
            exit=exit.title().strip()
            if lan=='ru':
                exit=translator(exit, 'en1')
            if exit=='Return':
                system('cls')
            else:
                print(translator('Goodbye!!!', lan))
                input(translator('Enter to exit: ', lan))
                break
        case _:
            system('cls')