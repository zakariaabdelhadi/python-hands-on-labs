import random

keeping = True

def dice_rolls(number_of_rolls = 8):

    if (number_of_rolls > 10):
        raise ValueError('must be less than 10 !')
    
    result_list = []
    for i in range(number_of_rolls):
        result_list.append(random.randint(1,6))

    return result_list    
    
while (keeping):
    number_of_dice_roll = input('how many dice to roll ? ')
    try:
        number = int(number_of_dice_roll)
    except:
        print('please enter a valid number')
        continue

    result_list = dice_rolls(number)
    somme = sum(result_list)
    print(*result_list,sep=', ', end=f'\t summe: ({str(somme)}) \n')

    prompt = input('do you want to quit ? (-1)')
    if (int(prompt) == -1):

        keeping = False
    else: continue    

