from random import randint
my_number = randint(1,10)
print(my_number)

keep_game = True

while(keep_game):
    user_input = input('please enter a number between 1 and 10 inklusiv: ')

    # if (isinstance(int(user_input),int) == False):
    #     print('please enter a valid number!')

    try:
        user_input = int(user_input)
    except ValueError: 
        print('please enter a valid number!')   
        continue 

    if (user_input == my_number):
        print('Bravoo !!')
    elif (user_input < my_number):
        print('le nombre est plus grand')
    else:
        print('le nombre est plus petit')   

    keeping = input(f'keep game ? (-1: quit, 00: keep): ')   
    if(int(keeping) == -1):  keep_game = False     