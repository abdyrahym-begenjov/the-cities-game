from translator import *
from random import choice
from propython import pywrite
from players import *

def play(obj, word, max_points, cities_list, cities_set, losers, have_winner, lang):
    if obj.out==False:
        while True:
            if word[-1] in ('ъ', 'ы', 'ь'):
                word=word[:-1]
            city=word
            print(word)
            word=input(f'[{obj.name}] {translator('You have', lang)} {obj.hearts} {translator('❤️. Enter the word: ', lang)}')
            word=word.title().strip()   
            if word=='':
                print(translator('You must enter the word!!!', lang))
                word=city
            elif word in cities_set:
                print(translator('This word has already been used.', lang))
                word=city
            elif word[0]==city[-1].upper() and word in cities_list and word not in cities_set:
                obj.points+=1
                cities_set.add(word)
                break
            else:
                print(translator('Error!!!', lang))
                obj.hearts-=1
                word=city
                break
        print(f'{translator('Points:', lang)} {obj.points}')
        if obj.points>=max_points:
            print(translator('You have received the maximum points', lang))
            print(translator('You are WINNER!!!', lang))
            have_winner=True
        if obj.hearts<=0:
            print(translator('You are eliminated from the game!!!', lang))
            print(f'{translator('You received', lang)} {obj.points} {translator('points.', lang)}')
            obj.out=True
            losers.append(obj.name)
        spisok2_result=(obj.points, obj.out, obj.hearts, word, cities_set, losers, have_winner)
    else:
        spisok2_result=(obj.points, obj.out, obj.hearts, word, cities_set, losers, have_winner)
    return spisok2_result