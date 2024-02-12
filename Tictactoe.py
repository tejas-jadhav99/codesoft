# TASK 2 - TIC-TAC-TOE AI

# Implement an AI agent that plays the classic game of Tic-Tac-Toe
# against a human player. You can use algorithms like Minimax with
# or without Alpha-Beta Pruning to make the AI player unbeatable.
# This project will help you understand game theory and basic search
# algorithms.


import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.ai_player = 'O'

    def print_board(self):
        for i in range(0, 9, 3):
            print(f'{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}')
            if i < 6:
                print('-' * 9)

    def is_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i*3 + j] == player for j in range(3)) or \
               all(self.board[j*3 + i] == player for j in range(3)):
                return True
        if all(self.board[i] == player for i in [0, 4, 8]) or \
           all(self.board[i] == player for i in [2, 4, 6]):
            return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_board_full()

    def get_empty_positions(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_player_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        else:
            print("Invalid move. Please choose an empty position.")
            return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def minimax(self, depth, maximizing_player):
        if self.is_winner('X'):
            return -1
        if self.is_winner('O'):
            return 1
        if self.is_board_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for position in self.get_empty_positions():
                self.board[position] = 'O'
                eval = self.minimax(depth + 1, False)
                self.board[position] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for position in self.get_empty_positions():
                self.board[position] = 'X'
                eval = self.minimax(depth + 1, True)
                self.board[position] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def get_best_move(self):
        best_val = float('-inf')
        best_move = -1

        for position in self.get_empty_positions():
            self.board[position] = 'O'
            move_val = self.minimax(0, False)
            self.board[position] = ' '

            if move_val > best_val:
                best_move = position
                best_val = move_val

        return best_move

def main():
    game = TicTacToe()

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', and the AI is 'O'.")
    print("Enter a number from 1 to 9 to make your move.")

    while not game.is_game_over():
        game.print_board()

        if game.current_player == 'X':
            try:
                user_move = int(input("Your move: ")) - 1
                if 0 <= user_move <= 8 and game.make_player_move(user_move):
                    game.switch_player()
                else:
                    continue
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 9.")
                continue
        else:
            ai_move = game.get_best_move()
            game.make_player_move(ai_move)
            game.switch_player()

    game.print_board()

    if game.is_winner('X'):
        print("You win! Congratulations!")
    elif game.is_winner('O'):
        print("AI wins! Better luck next time.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
