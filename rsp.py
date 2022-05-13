import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    # Initializer
    def __init__(self):
        # Player Score
        self.score = 0
        # Movement of player
        self.proceed = ''

    # Move Selection
    def move(self):
        # This move will always select rock
        self.proceed = 'rock'
        return self.proceed

    # Learn move of the other player
    def learn(self, move1):
        pass

    # Check if the other player was beaten
    def beats(self, two):
        return ((self.proceed == 'rock' and two == 'scissors') or
                (self.proceed == 'scissors' and two == 'paper') or
                (self.proceed == 'paper' and two == 'rock'))


class AllRockPlayer (Player):

    # Initializer
    def __init__(self):
        # Player Score
        self.score = 0
        # Movement of player
        self.proceed = ''

    # Move Selection
    def move(self):
        # This move will always select rock
        self.proceed = 'rock'
        return self.proceed

    # Learn move of the other player
    def learn(self, move1):
        pass

    # Check if the other player was beaten
    def beats(self, two):
        return ((self.proceed == 'rock' and two == 'scissors') or
                (self.proceed == 'scissors' and two == 'paper') or
                (self.proceed == 'paper' and two == 'rock'))


class RandomPlayer(Player):

    # Initializer
    def __init__(self):
        super().__init__()

    # Move Selection
    def move(self):
        self.proceed = random.choice(moves)
        return self.proceed

    # Check if the other player was beaten
    def beats(self, two):
        return ((self.proceed == 'rock' and two == 'scissors') or
                (self.proceed == 'scissors' and two == 'paper') or
                (self.proceed == 'paper' and two == 'rock'))

    # Learn move of the other player
    def learn(self, move1):
        pass


class HumanPlayer(Player):

    # Initializer
    def __init__(self):
        super().__init__()

    # Move Selection
    def move(self):
        while True:
            self.proceed = input("Rock, paper, scissors? > ").lower()
            if self.proceed in moves:
                return self.proceed

    def beats(self, two):  # Check if the other player was beaten
        return ((self.proceed == 'rock' and two == 'scissors') or
                (self.proceed == 'scissors' and two == 'paper') or
                (self.proceed == 'paper' and two == 'rock'))


class CyclePlayer(Player):

    # Initializer
    def __init__(self):
        super().__init__()

    # Move Selection
    def move(self):
        if self.proceed == '':
            self.proceed = 'rock'
            return self.proceed
        if self.proceed == 'rock':
            self.proceed = 'paper'
            return self.proceed
        if self.proceed == 'paper':
            self.proceed = 'scissors'
            return self.proceed
        if self.proceed == 'scissors':
            self.proceed = 'rock'
            return self.proceed

    # Check if the other player was beaten
    def beats(self, two):
        return ((self.proceed == 'rock' and two == 'scissors') or
                (self.proceed == 'scissors' and two == 'paper') or
                (self.proceed == 'paper' and two == 'rock'))

    # Learn move of the other player
    def learn(self, move1):
        pass


class ReflectPlayer(Player):

    # Initializer
    def __init__(self):
        super().__init__()
        self.reflect_move = ''

    # Move Selection
    def move(self):
        if self.reflect_move == '':
            self.proceed = random.choice(moves)
            return self.proceed
        else:
            self.proceed = self.reflect_move
            return self.proceed

    # Learn move of the other player
    def learn(self, move1):
        self.reflect_move = move1

    # Check if the other player was beaten
    def beats(self, two):
        return ((self.proceed == 'rock' and two == 'scissors') or
                (self.proceed == 'scissors' and two == 'paper') or
                (self.proceed == 'paper' and two == 'rock'))


class Game:

    # Initializer
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # To get game status
    def game_play(self, game_play_status):
        print("====================")
        print("GAME: " + game_play_status + "!")
        print("====================")

    # Check for the winner
    def check_winner(self, val1, val2):
        if val1 == val2:
            print("** DRAW **")
            print(f"""Score: Player One {self.p1.score}, """ +
                  f"""Player Two {self.p2.score}""")
        elif val1:
            print("** PLAYER ONE WINS **")
            self.p1.score += 1
            print(f"""Score: Player One {self.p1.score}, """ +
                  f"""Player Two {self.p2.score}""")
        elif val2:
            print("** PLAYER TWO WINS **")
            self.p2.score += 1
            print(f"""Score: Player One {self.p1.score}, """ +
                  f"""Player Two {self.p2.score}""")

    # Player one plays
    def play_round(self):
        move1 = self.p1.move()
        print(f"You played {self.p1.proceed}.")
        # Player two plays
        move2 = self.p2.move()
        self.p2.learn(move1)
        print(f"Opponent played {self.p2.proceed}.")
        # To determine if player1 beats player2
        check_player1 = self.p1.beats(self.p2.proceed)
        # To determine if player2 beats player1
        check_player2 = self.p2.beats(self.p1.proceed)
        # Then this determine the winner between player1 and player2
        self.check_winner(check_player1, check_player2)

    def display_winner(self):
        print("*** TOTAL SCORE ***")
        print(f"PLAYER ONE: {self.p1.score}\nPLAYER TWO: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("PLAYER ONE WINS!")
        elif self.p1.score < self.p2.score:
            print("PLAYER TWO WINS")
        else:
            print("THE GAME ENDED IN A DRAW")

    def play_game(self, number_round):
        self.game_play('Game start')
        for round in range(number_round):
            print(f"Round {round + 1} --:")
            self.play_round()
        self.game_play('Game over!')
        self.display_winner()


if __name__ == '__main__':

    other_player = [RandomPlayer(), ReflectPlayer(), CyclePlayer(),
                    AllRockPlayer()]

    while True:
        try:
            number_round = input("How many rounds would you like to play? ")
            int_num = int(number_round)
            if isinstance(int_num, int):
                randomNumber = random.randint(0, 3)
                game = Game(HumanPlayer(), other_player[randomNumber])
                game.play_game(int_num)
                break
        # Informs player to put in the correct value
        except ValueError:
            print("Please enter a value")
            continue
