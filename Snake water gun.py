#Snake water gun game
import random
l = ['S', 'W', 'G']
name = input('Please enter your name: ')
print('Welcome!',name)
cpu_count = 0
user_count = 0
i = 0
while i<10:
    cpu = random.choice(l)
    user = input('Enter your choice:\nSnake: S\nWater: W\nGun: G\n ').upper()
    if user == 'S' and cpu == 'W':
        user_count += 1
    elif user == 'S' and cpu == 'G':
        cpu_count += 1
    elif user == 'W' and cpu == 'S':
        cpu_count += 1
    elif user == 'W' and cpu == 'G':
        user_count += 1
    elif user == 'G' and cpu == 'S':
        cpu_count += 1
    elif user == 'G' and cpu == 'W':
        cpu_count += 1
    elif user == 'S' and cpu == 'S':
        user_count+=1
        cpu_count+=1
    elif user == 'W' and cpu == 'W':
        user_count+=1
        cpu_count+=1
    elif user == 'G' and cpu == 'G':
        user_count+=1
        cpu_count+=1
    else:
        print('Wrong input')

    i+=1
print('cpu', cpu_count)
print('user', user_count)
if cpu_count == user_count:
    print('Game tied')
elif cpu_count > user_count:
    print('Sorry!', name, 'You lose')
else:
    print('Congratulations!', name, 'You Win')



