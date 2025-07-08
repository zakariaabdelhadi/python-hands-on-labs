def get_user_input(word_art):
    return input(f'please enter a {word_art}: ')

noun = get_user_input('noun')
verb = get_user_input('verb')
adjektiv = get_user_input('adjektiv')

print(f'hello {noun}. you must {verb}. because you are {adjektiv}')