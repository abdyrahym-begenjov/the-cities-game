from random import choice
from propython import pyread, pywrite
from time import sleep
from translator import *
from utils import *
from players import *
from play import *

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
            while True:
                print(translator('Infinity          Party', lang))
                mode_game=input(translator('Choose a game mode: ', lang))
                mode_game=new_word(mode_game, lang)
                if mode_game=='Infinity' or mode_game=='Party':
                    break
            clear_screen()

            if mode_game=='Party':
                p=[translator('Player 2', lang), translator('Player 3', lang), translator('Player 4', lang)]
                lst1=[name]
                while True:
                    game_count=input(translator('Enter number of the players: ', lang))
                    if game_count in ('2', '3', '4'):
                        try:
                            game_count=int(game_count)
                            break
                        except ValueError:
                            print(translator('Error!!!', lang))
                    else:
                        print(translator('Error!!!', lang))

                max_points=choose_parameter(lang)
                clear_screen()
                for _ in range(game_count-1):
                    lst1.append(game(p, lst1, base, lang))
                
                result1=selection_of_order(lst1, game_count, lang, Player)
                for n, i in enumerate(result1, 1):
                    print(f'{n}) {i.name}')
                
                start=input(translator('Enter to start game: ', lang))
                print(translator('Loading...', lang))
                sleep(2)
                clear_screen()

                final=False
                city=choice(cities_list)
                number=1
                cities_set=set()
                have_winner=False
                losers=[]

                while True:
                    for player in result1:
                        player.points, player.out, player.hearts, city, cities_set, losers, have_winner=play(player, city, max_points, cities_list, cities_set, losers, have_winner, lang)
                        if have_winner==True:
                            final=have_winner
                            break
                    spisok=[]
                    for player in result1:
                        spisok.append((player.name, player.points))
                    spisok.sort(key=lambda x: x[1], reverse=True)
                    spisok1=list(map(lambda x: x[0], spisok))
                    spisok2=list(map(lambda x: x[1], spisok))
                    if final==True or len(losers)==game_count-1:
                        if game_count==2:
                            print(f'1) {spisok1[0]} - {translator('WINNER', lang)} 😎🏆. Points: {spisok2[0]}')
                            print(f'2) {spisok1[1]} - {translator('LOSER', lang)} 😫. Points: {spisok2[1]}')
                            break
                        elif game_count==3:
                            print(f'1) {spisok1[0]} - {translator('WINNER', lang)} 😎🏆. Points: {spisok2[0]}')
                            print(f'2) {spisok1[1]} - {translator('ROUND-UP', lang)} 😀. Points: {spisok2[1]}')
                            print(f'3) {spisok1[2]} - {translator('LOSER', lang)} 😫. Points: {spisok2[2]}')
                            break
                        elif game_count==4:
                            print(f'1) {spisok1[0]} - {translator('WINNER', lang)} 😎🏆. Points: {spisok2[0]}')
                            print(f'2) {spisok1[1]} - {translator('ROUND-UP', lang)} 😀. Points: {spisok2[1]}')
                            print(f'3) {spisok1[2]} - {translator('BRONZE MEDALIST', lang)} 😐. Points: {spisok2[2]}')
                            print(f'4) {spisok1[3]} - {translator('LOSER', lang)} 😫. Points: {spisok2[3]}')
                            break
                    
                for player in result1:
                    if player.name not in base:
                        base[player.name]=0
                    base[player.name]+=player.points
                pywrite('base.json', base)
                    
            else:
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