#Guessing the number
nam = input('Enter your name: ')
print('Welcome to guessing game', nam)
num = 18
i = 0
while(True):
    count = 9 - i
    if count<0:
        print('Game over')
        break
    i += 1

    val = int(input('Enter a number: '))
    if val>18:
        if val>30:
            print('You are guessing much bigger, guess near 25')
        if val==19:
            print('You are close')
        print('Guess a smaller number')
    elif val<18:
        if val <10:
            print('You are guessing much smaller')
        print('Guess a bigger number')
    else:
        print('Congrats! you guessed it correctly')
        break
    print("left count=", count)

















