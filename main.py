import random
import os
clear = lambda: os.system('clear')


class Game:

    def __init__(self):
        self.num_pool = [n for n in range(1, 76)]
        self.print_pool = [n for n in range(1, 76)]

    def draw(self):
        drawn_num = random.choice(self.num_pool)
        self.num_pool.remove(drawn_num)
        if drawn_num >= 10:
            self.print_pool[drawn_num - 1] = "  "
        else:
            self.print_pool[drawn_num - 1] = " "

        if drawn_num <= 15:
            letter = 'B'
            print(f'{letter}-{drawn_num}')
            return
        if drawn_num <= 30:
            letter = 'I'
            print(f'{letter}-{drawn_num}')
            return
        if drawn_num <= 45:
            letter = 'N'
            print(f'{letter}-{drawn_num}')
            return
        if drawn_num <= 60:
            letter = 'G'
            print(f'{letter}-{drawn_num}')
            return
        else:
            letter = 'O'
            print(f'{letter}-{drawn_num}')
            return

    def print_board(self):
        print("B   I   N   G   O\n")

        for n in range(0, 15):
            if len(str(self.print_pool[n])) == 1:
                print(f'{self.print_pool[n]}   ', end='')
            else:
                print(f'{self.print_pool[n]}  ', end='')
            print(f'{self.print_pool[n + 15]}  '
                  f'{self.print_pool[n + 30]}  '
                  f'{self.print_pool[n + 45]}  '
                  f'{self.print_pool[n + 60]}')

        print("\n")
        print(f'Remaining: {len(self.num_pool)}')
        print('Press enter to continue. Type \'reset\' to restart the game or \'exit\' to quit.')


def play():
    clear()
    bingo = Game()
    print('Let\'s play Bingo! Press enter to begin')
    while len(bingo.num_pool) > 0:
        turn = input()
        clear()
        if turn.lower() == 'reset':
            play()
        if turn.lower() == 'exit':
            exit()
        bingo.draw()
        print('\n')
        bingo.print_board()
        print('\n')
    while True:
        response = input('The game has ended. Type \'reset\' to restart the game or \'exit\' to quit:  ')
        if response.lower() == 'reset':
            play()
        if response.lower() == 'exit':
            exit()


play()