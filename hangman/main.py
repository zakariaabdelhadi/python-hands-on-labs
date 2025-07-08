from random import choice

secret_word = choice(['apple', 'secret', 'banana'])
semi_secret_word = list('-'*len(secret_word))
number_of_tries = 3
player_name = input('enter your name: ')
print('welcome to hangman game ' + player_name)


while (number_of_tries > 0):

    print('Word: ',end='')
    print(*semi_secret_word)

    letter = input('enter a letter: ')
    if(letter in secret_word):
        positions = [i for i, c in enumerate(secret_word) if c == letter]
        position_in_word = secret_word.find(letter)
        for i in positions:
          semi_secret_word[i] = letter   

    else: 
        print('makaynach')
        number_of_tries -= 1   

    if('-' not  in semi_secret_word or letter == secret_word):
        print('you won !!')
        break     

if(number_of_tries == 0):
    print("you lose !!")