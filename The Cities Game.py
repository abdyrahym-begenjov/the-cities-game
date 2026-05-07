from random import choice
from propython import pyread
from time import sleep
from translator import *

print('English |  Русский')
while True:
    choose_language=input()
    choose_language=choose_language.title().strip()
    if choose_language=='English' or choose_language=='Русский':
        break

match choose_language:
    case 'Русский':
        lan='ru'
        cities_list=pyread('new cities.json')
    case 'English':
        lan='en'
        cities_list=pyread('cities.json')

print(translator('The Cities Game', lan))
print(f'{translator('Creator: Abdyrahym Begenjov', lan)}     (GitHub: abdyrahym-begenjov)')
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

end=input(translator('Enter to exit: ', lan))