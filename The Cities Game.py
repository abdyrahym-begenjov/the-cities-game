from random import choice
from propython import pyread
from time import sleep

print('The Cities Game')
print('Creator: Abdyrahym Begenjov (GitHub: abdyrahym-begenjov)')
start=input('Enter to start game: ')
print('Loading...')
sleep(2)

cities_list=pyread('cities.json')

word=choice(cities_list)
heart=3
points=0
number=1
cities_set=set()

print(f'{number}) {word}')

while True:
    city=word
    word=input(f'You have {heart} hearts. Enter the word: ')
    word=word.title().strip()
    if heart==1:
        print('Game Over!!!')
        print(f'You received {points}')
        match points:
            case n if n>=60:
                print('Absolute Champion!!! 🏆')
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
                print('Loser!!!')
        break
    elif word=='':
        print('You must enter the city!!!')
        print('Error!!!')
        heart-=1
        word=city
    elif word[0]==city[-1].upper() and word in cities_list and word not in cities_set:
        number+=1
        print(f'{number}) {word}')
        points+=1
        cities_set.add(word)
    else:
        if word in cities_set:
            print('This word has already been used.')
        print('Error!!!')
        print(word)
        heart-=1
        word=word[0]

end=input('Enter to quit: ')