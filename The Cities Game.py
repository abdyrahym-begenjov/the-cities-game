from propython import pyread
from translator import *
from utils import *
from mode_functions import *

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
        base[name]=[0, 0]

    print(translator('The Cities Game 🏙️', lang))
    print(f'{translator('Creator: Abdyrahym Begenjov', lang)}     (GitHub: abdyrahym-begenjov)')
    print(translator('Game      Rules      Highscores      Settings      Exit', lang))
    mode=input(translator('Choose a game mode: ', lang))
    mode=new_word(mode, lang)
    clear_screen()
    match mode:
        case 'Game':
            while True:
                print(translator('Infinity          Party', lang))
                mode_game=input(translator('Choose a game mode: ', lang))
                mode_game=new_word(mode_game, lang)
                if mode_game=='Infinity' or mode_game=='Party':
                    break
            clear_screen()

            if mode_game=='Party':
                mode_party(name, cities_list, base, lang)       
            else:
                mode_infinity(name, cities_list, base, lang)

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