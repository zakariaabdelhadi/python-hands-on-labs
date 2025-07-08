import emoji
import random
import sys


class Rps:
    robot_winn_counter = 0
    user_winn_counter = 0
    def __init__(self):
        self.moves = {"stein": emoji.emojize(":rock:"), "papier": emoji.emojize(":page_with_curl:"), "scheere": emoji.emojize(":scissors:")}
        self.valid_moves = list(self.moves.keys())

    def play_game(self):
        user_move = input('please ein Move eingeben (stein, scheere, papier): ').lower()

        if (user_move == 'exit'):
            print('danke fürs Spielen..Tschüss')
            sys.exit()

        if(user_move not in self.valid_moves):
            print('please enter a valid move..')
            return self.play_game()

        random_move = random.choice(self.valid_moves)    
    
        self.print_game(user_move, random_move)
        self.check_game(user_move, random_move)

        print(f'User winn: {self.__class__.user_winn_counter}')
        print(f'Robot winn: {self.__class__.robot_winn_counter}')


    def check_game(self, user_move, random_move):
        # The game logic
        if user_move == random_move:
            print('It is a tie!')
        elif user_move == 'stein' and random_move == 'scheere':
            print('You win!')
            self.__class__.user_winn_counter += 1
        elif user_move == 'scheere' and random_move == 'papier':
            print('You win!')
            self.__class__.user_winn_counter += 1
        elif user_move == 'papier' and random_move == 'stein':
            print('You win!')
            self.__class__. user_winn_counter += 1
        else:
            print('Robot wins...')
            self.__class__.robot_winn_counter += 1
 

    def print_game(self, user_move, random_move):
        print(f'User: {self.moves[user_move]}')
        print(f'Robot: {self.moves[random_move]}')



# rps = Rps()
# print(rps.moves['Stein'])        
# print(rps.valid_moves)        
if __name__ == '__main__':
    rps = Rps()

    while(True):
        rps.play_game()
