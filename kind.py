#!/usr/bin/env python3
import random

moves = ['rock', 'paper', 'scissors']
options = ['random', 'reflect', 'repeat', 'cycle']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.index = 0

    def move(self):
        if self.index == 0:
            self.index += 1
            return random.choice(moves)
        else:
            return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = their_move


class HumanPlayer(Player):
    def move(self):
        user_move = input('Enter your move (' +
                          ', '.join(moves) + '):\n')
        while user_move not in moves:
            user_move = input("Invalid move, try again\n")
        return user_move


class CyclePlayer(Player):
    def __init__(self):
        self.last_move = 0

    def move(self):
        if self.last_move < 2:
            self.last_move += 1
        else:
            self.last_move = 0
        return moves[self.last_move]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if (move1 == move2):
            print("it's a tie!")
        elif ((move1 == "rock") and (move2 == "scissors")):
            self.p1_score += 1
            print("Horray ! You win!")
        elif ((move1 == "paper") and (move2 == "rock")):
            self.p1_score += 1
            print("Horray ! You win!")
        elif ((move1 == "scissors") and (move2 == "paper")):
            self.p1_score += 1
            print("Horray ! You win!")
        elif ((move2 == "rock") and (move1 == "scissors")):
            self.p2_score += 1
            print("You lose!")
        elif ((move2 == "paper") and (move1 == "rock")):
            self.p2_score += 1
            print("You lose!")
        elif ((move2 == "scissors") and (move1 == "paper")):
            self.p2_score += 1
            print("You lose!")
        print(f"Score: Player One {self.p1_score}, Player Two {self.p2_score}")

    def play_game(self):
        print("Game start!")
        while True:
            try:
                round = int(input("How many rounds would you like to play?"))
            except ValueError:
                print("Please enter a number!")
            else:
                break
        for i in range(round):
            print(f"Round {i}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    user_choice = input('Choose a version (' +
                        ', '.join(options) + '):\n')
    while user_choice not in options:
        user_choice = input("Invalid choice, try again\n")

    if user_choice == "random":
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
    elif user_choice == "reflect":
        game = Game(HumanPlayer(), ReflectPlayer())
        game.play_game()
    elif user_choice == "repeat":
        game = Game(HumanPlayer(), Player())
        game.play_game()
    elif user_choice == "cycle":
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()
