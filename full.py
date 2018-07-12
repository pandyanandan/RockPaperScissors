'''
Rock Paper Scissors

Rules:
Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins

 1 = Rock
 2 = Paper
 3 = Scissors

 For best results please use repl.it

 if program not running install following pagkage `termcolor`
 https://pypi.org/project/termcolor/#description
'''

import random
from termcolor import cprint


class Game(object):
    def __init__(self, Rounds):
        self._human_CurrentScore = 0
        self._cpu_CurrentScore = 0
        self._Rounds = Rounds

    def SingleRound(self):
        name = input("Enter name:")
        human = HumanPlayer(name)
        human.move()
        cpu = RandomPlayer("CPU1", human.returnChoice())
        cpu.move()
        self.CheckWinner(human.returnChoice(), cpu.getChoice())

    def MultipleRounds(self, Rounds):
        i = 1
        while i <= Rounds:
            self.SingleRound()
            i = i + 1
        self.DisplayScoreRound()

    def SingleRoundRock(self):
        name = input("Enter name:")
        human = HumanPlayer(name)
        human.move()
        cpu = AllRockerPlayer("CPU1", human.returnChoice())
        cpu.move()
        self.CheckWinner(human.returnChoice(), 1)

    def MultipleRoundsRock(self, Rounds):
        i = 1
        while i <= Rounds:
            self.SingleRoundRock()
            i = i + 1
        self.DisplayScoreRound()

    def MultipleRoundsCycle(self, Rounds):
        i = 1
        human = HumanPlayer("abc")
        cpu = CyclePlayer("CPU1", 1)
        while i <= Rounds:
            name = input("Enter name:")
            human = HumanPlayer(name)
            human.move()
            self.CheckWinner(human.returnChoice(), cpu.move())
            i = i + 1
        self.DisplayScoreRound()

    def MultipleRoundsReflect(self, Rounds):
        i = 1
        human = HumanPlayer("abc")
        cpu = ReflectPlayer("CPU1", 1)
        human_choice = 0
        while i <= Rounds:
            name = input("Enter name:")
            human = HumanPlayer(name)
            human.move()
            cpu_move = cpu.move()
            cpu.remember(human.returnChoice())
            self.CheckWinner(human.returnChoice(), cpu_move)
            i = i + 1
        self.DisplayScoreRound()

    def CheckWinner(self, h, c):
        cprint("Your Choice:" + str(h), 'blue')
        cprint("CPU Choice" + str(c), 'blue')
        if h == c:
            cprint("It's Tie both are winner", 'magenta')
        elif h == 2 and c == 1 or c == 2 and h == 1:
            if c == 2:
                cprint("Paper beats Rock: CPU wins", 'magenta')
                self._cpu_CurrentScore = self._cpu_CurrentScore + 1
            elif h == 2:
                cprint("Paper beats Rock: You win!", 'magenta')
                self._human_CurrentScore = self._human_CurrentScore + 1
        elif h == 1 and c == 3 or c == 1 and h == 3:
            if c == 1:
                cprint("Rock beats Scissor: CPU wins", 'magenta')
                self._cpu_CurrentScore = self._cpu_CurrentScore + 1
            elif h == 1:
                cprint("Rock beats Scissors: You win!", 'magenta')
                self._human_CurrentScore = self._human_CurrentScore + 1
        elif h == 2 and c == 3 or c == 2 and h == 3:
            if c == 3:
                cprint("Scissors beats Paper: CPU wins", 'magenta')
                self._cpu_CurrentScore = self._cpu_CurrentScore + 1
            elif h == 3:
                cprint("Scissors beats Paper: You win!", 'magenta')
                self._human_CurrentScore = self._human_CurrentScore + 1

    def DisplayScoreRound(self):
        cprint("CPU Score :" + str(self._cpu_CurrentScore),
               'grey', 'on_magenta')
        cprint("Your Score :" + str(self._human_CurrentScore),
               'grey', 'on_magenta')
        if self._cpu_CurrentScore > self._human_CurrentScore:
            cprint("Final Winner is CPU With :" + str(self._cpu_CurrentScore),
                   'cyan', attrs=['blink'])
        else:
            cprint("You are final Winner With :" +
                   str(self._human_CurrentScore), 'cyan', attrs=['blink'])


class Player(object):

    def __init__(self, Name, Choice):
        self._Name = Name
        self._Choice = Choice


class HumanPlayer(Player):

    def __init__(self, Name):
        self._Name = Name
        self._Choice = 0

    def returnChoice(self):
        return self._Choice

    def move(self):
        while True:
            self._Choice = input("Enter choice \n 1. Rock \n 2. Paper" +
                                 "\n 3. Scissor \n")
            if not self._Choice.isdigit():
                cprint("Please Enter Valid Choice !", 'red')
                continue
            else:
                self._Choice = int(self._Choice)
            if 0 < self._Choice < 4:
                super(HumanPlayer, self).__init__(self._Name, self._Choice)
                break
            else:
                cprint("Please Enter Valid Choice !", 'red')
                continue

    def remember(self):
        return


class RandomPlayer(Player):
    def __init__(self, Name, Choice):
        self._Name = Name
        self._Choice = Choice
        super(RandomPlayer, self).__init__(self._Name, self._Choice)

    def move(self):
        move = random.randint(1, 3)
        self._Choice = move
        return move

    def getChoice(self):
        return self._Choice

    def remember(self):
        return


class ReflectPlayer(Player):

    def __init__(self, Name, Choice):
        self._Name = Name
        self._Choice = Choice
        self._last_move = Choice
        super(ReflectPlayer, self).__init__(self._Name, self._Choice)

    def move(self):
        return self._last_move

    def remember(self, lmove):
        self._last_move = lmove


class AllRockerPlayer(Player):
    def __init__(self, Name, Choice):
        self._Name = Name
        self._Choice = Choice
        super(AllRockerPlayer, self).__init__(self._Name, self._Choice)

    def move(self):
        return int(1)

    def remember(self):
        return


class CyclePlayer(Player):
    _last_move = 0

    def __init__(self, Name, Choice):
        self._Name = Name
        self._Choice = Choice
        super(CyclePlayer, self).__init__(self._Name, self._Choice)

    def move(self):
        move = 0
        if self._last_move == 0:
            move = 1
        elif self._last_move == 1:
            move = 2
        else:
            move = 3
        self._last_move += 1
        if self._last_move >= 3:
            self._last_move = 0
        return move

    def remember(self):
        return


def Start():
    cprint("Winning Rules of the Rock paper scissor game as follows: \n"
           + "Rock vs paper->paper wins \n"
           + "Rock vs scissor->Rock wins \n"
           + "paper vs scissor->scissor wins \n", 'green')
    while True:
        GameType = int(input("1. Single Round (Human vs Random)" +
                             "\n2. Multiple Rounds(Human vs Random)" +
                             "\n3. Multiple Rounds(Human vs Always Rock)" +
                             "\n4. Multiple Rounds(Human vs Copy)" +
                             "\n5. Multiple Rounds(Human vs Cycle)"))
        if 0 < GameType < 6:
            if GameType == 1:
                g = Game(1)
                g.SingleRound()
                break
            elif GameType == 2:
                while True:
                    GameRounds = int(input("How Many Rounds Would you Like to"
                                           + "play ?(Maximum 3)"))
                    if 0 < GameRounds < 4:
                        g = Game(GameRounds)
                        g.MultipleRounds(GameRounds)
                        break
                    else:
                        cprint("Please Enter Valid number !", 'red')
                        continue
                break
            elif GameType == 3:
                while True:
                    GameRounds = int(input("How Many Rounds Would you Like to"
                                           + "play ?(Maximum 3)"))
                    if 0 < GameRounds < 4:
                        g = Game(GameRounds)
                        g.MultipleRoundsRock(GameRounds)
                        break
                    else:
                        cprint("Please Enter Valid number !", 'red')
                        continue
                break
            elif GameType == 4:
                while True:
                    GameRounds = int(input("How Many Rounds Would you Like to"
                                           + "play ?(Maximum 3)"))
                    if 0 < GameRounds < 4:
                        g = Game(GameRounds)
                        g.MultipleRoundsReflect(GameRounds)
                        break
                    else:
                        cprint("Please Enter Valid number !", 'red')
                        continue
                break
            elif GameType == 5:
                while True:
                    GameRounds = int(input("How Many Rounds Would you Like to"
                                           + "play ?(Maximum 3)"))
                    if 0 < GameRounds < 4:
                        g = Game(GameRounds)
                        g.MultipleRoundsCycle(GameRounds)
                        break
                    else:
                        cprint("Please Enter Valid number !", 'red')
                        continue
                break
        else:
            cprint("Please Enter Valid number !", 'red')
            continue


Start()
