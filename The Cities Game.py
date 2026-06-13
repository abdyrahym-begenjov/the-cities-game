from random import choice
from propython import pyread, pywrite
from time import sleep
from translator import *
from utils import *

while True:
    base=pyread('base.json')
    data=pyread('data.json')

    name=data['name']
    lang=data['language']
    cities_list=data['cities']

    if lang=='' and cities_list==[]:
        lang, cities_list=enter_lang(data)
        clear_screen()

    if name=='':
        name=enter_name(data, lang)
        clear_screen()
    
    if name not in base:
        base[name]=0

    print(translator('The Cities Game 🏙️', lang))
    print(f'{translator('Creator: Abdyrahym Begenjov', lang)}     (GitHub: abdyrahym-begenjov)')
    print(translator('Game      Rules      Highscores      Settings      Exit', lang))
    mode=input(translator('Choose a game mode: ', lang))
    mode=new_word(mode, lang)
    clear_screen()
    match mode:
        case 'Game':
            start=input(translator('Enter to start game: ', lang))
            print(translator('Loading...', lang))
            sleep(2)
            clear_screen()

            word=choice(cities_list)
            hearts=3
            points=0
            number=1
            cities_set=set()

            while True:
                if word[-1] in ('ъ', 'ы', 'ь'):
                    word=word[:-1]
                city=word
                if len(cities_set)==len(cities_list):
                    print(translator('You are ABSOLUTE CHAMPION!!!', lang))
                    print(f'{translator('You received', lang)} {points} {translator('points.', lang)}')
                    print(star(points, lang))
                    break
                if hearts!=0:
                    print(f'{number}) {word}')
                    word=input(f'{translator('You have', lang)} {hearts} {translator('❤️. Enter the word: ', lang)}')
                    word=word.title().strip()
                if hearts<=0:
                    print(translator('Game Over!!!', lang))
                    print(f'{translator('You received', lang)} {points} {translator('points.', lang)}')
                    print(star(points, lang))
                    break    
                elif word=='':
                    print(translator('You must enter the word!!!', lang))
                    word=city
                elif word in cities_set:
                    print(translator('This word has already been used.', lang))
                    word=city
                elif word[0]==city[-1].upper() and word in cities_list and word not in cities_set:
                    number+=1
                    points+=1
                    cities_set.add(word)
                else:
                    print(translator('Error!!!', lang))
                    hearts-=1
                    word=city
            
            if base[name]<points:
                print(translator('You\'ve broken a new highscore!!!', lang))
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

        case 'Highscores':
            draw_leaderboard(base, lang)
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()
    
        case 'Settings':
            while True:
                print(f'{translator('Name', lang)}: {data['name']}')
                print(f'{translator('Language', lang)}: {data['language']}')
                change=input(translator('Do you want to change parameters (Enter \"Name\" or \"Language\"): ', lang))
                change=new_word(change, lang)
                match change:
                    case 'Name':
                        name=enter_name(data, lang)
                        clear_screen()
                    case 'Language':
                        lang, cities_list=enter_lang(data)
                        clear_screen()
                    case _:
                        break
            clear_screen()

        case 'Exit':
            exit_confirm=input(translator('Do you want to exit (\"Yes\" or \"No\"): ', lang))
            exit_confirm=new_word(exit_confirm, lang)
            if exit_confirm=='No':
                clear_screen()
            else:
                print(translator('Goodbye!!!', lang))
                input(translator('Enter to exit: ', lang))
                break
        case _:
            clear_screen()