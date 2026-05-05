from random import choice
from json import load

with open('cities.json', 'r', encoding='utf-8') as i:
    cities_list=load(i)

word=choice(cities_list)
heart=3
points=0
number=1
cities_set=set()

print(f'{number}) {word}')

while True:
    city=word
    word=input(f'You have {heart} hearts. Enter the word: ')
    if word=='':
        word='Error!!!'
    word=word.title().strip()
    if word[0]==city[-1].upper() and word in cities_list and word not in cities_set:
        number+=1
        print(f'{number}) {word}')
        points+=1
        cities_set.add(word)
    elif heart==1:
        print('Game Over!!!')
        print(f'You received {points}')
        match points:
            case n if n>=10:
                print('⭐')
            case n if n>=20:
                print('⭐⭐')
            case n if n>=30:
                print('⭐⭐⭐')
            case n if n>=40:
                print('⭐⭐⭐⭐')
            case n if n>=50:
                print('⭐⭐⭐⭐⭐')
            case n if n>=60:
                print('Absolute Champion!!! 🏆')
            case _:
                print('Loser!!!')
        break
    else:
        if word in cities_set:
            print('This word has already been used.')
        print('Error!!!')
        print(word)
        heart-=1
        word=word[0]