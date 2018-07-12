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

h_choice = 1
roto = 1


class Game(object):
    def __init__(self, Rounds):
        self._human_CurrentScore = 0
        self._cpu_CurrentScore = 0
        self._Rounds = Rounds

    def SingleRound(self):
        name = input("Enter name:")
        while True:
            c = input("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n")
            if not c.isdigit():
                cprint("Please Enter Valid Choice !", 'red')
                continue
            else:
                c = int(c)
            if 0 < c < 4:
                Human(name, c)
                break
            else:
                cprint("Please Enter Valid Choice !", 'red')
                continue
        cpu = CPU("CPU1", 1)
        cpu.remember(c)
        self.CheckWinner(c, cpu.getChoice())

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

    def MultipleRounds(self, Rounds):
        i = 1
        while i <= Rounds:
            self.SingleRound()
            i = i + 1
        self.DisplayScoreRound()

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


class Human(Player):

    def __init__(self, Name, Choice):
        super(Human, self).__init__(Name, Choice)


class CPU(Player):

    def __init__(self, Name, Choice):
        self._Name = Name
        self._Choice = Choice
        self.move()
        super(CPU, self).__init__(self._Name, self._Choice)

    def move(self):
        selection = random.randint(1, 4)
        if selection == 1:
            self._Choice = self.strategy1()
        elif selection == 2:
            self._Choice = self.strategy2()
        elif selection == 3:
            self._Choice = self.strategy3()
        else:
            self._Choice = self.strategy4(roto)

    def strategy1(self):
        return int(1)

    def strategy2(self):
        return int(random.randint(1, 3))

    def strategy3(self):
        return int(h_choice)

    def strategy4(self, roto1):
        global roto
        if roto1 == 1 or roto1 == 2:
            roto = roto + 1
            return int(roto1)
        if roto == 3:
            roto = 1
            return int(3)

    def getChoice(self):
        return self._Choice

    def remember(self, l_h_choice):
        global h_choice
        h_choice = l_h_choice


def Start():
    cprint("Winning Rules of the Rock paper scissor game as follows: \n"
           + "Rock vs paper->paper wins \n"
           + "Rock vs scissor->Rock wins \n"
           + "paper vs scissor->scissor wins \n", 'green')
    while True:
        GameType = int(input("1. Single Round \n2. Multiple Rounds"))
        if 0 < GameType < 3:
            if GameType == 1:
                g = Game(1)
                g.SingleRound()
                break
            else:
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
        else:
            cprint("Please Enter Valid number !", 'red')
            continue


Start()
