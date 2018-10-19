# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
import numpy as np
import random
from random import randint

class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args

    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """
        # return Directions.STOP
        legals = state.getLegalActions()
        legals.remove(Directions.STOP)

        # print(state.getFood())
        # print("\n")
        # print(state.getWalls())

        # print(state.getPacmanPosition())
        print(state.generatePacmanSuccessors())

        action = legals[self.select_best_move(legals, state)]
        print(action)

        return action

    def select_best_move(self, legals, state):
        # python run.py --agentfile pacmanagent.py # --layout large
        # random.seed(123)
        currentFood = list(state.getFood())

        print("# of Food -> ", state.getNumFood())

        posFood = []
        # print(currentFood.width)
        # print(currentFood.height)
        # print(len(currentFood))
        # print(len(currentFood[0]))

        for i in range(len(currentFood)): # columns
            for j in  range(len(currentFood[0])): # rows
                if currentFood[i][j] == True:
                    # print("the other one -> ", currentFood[i][j], i, j)
                    posFood.append((i,j))
        # posFood = [[(i,j) for j in range(len(currentFood[0])) if currentFood[i][j] == True] for i in range(len(currentFood))]
        # print(posFood)
        # print("Shape of posFood",np.shape(posFood))
        distances = self.get_distances(posFood, state.getPacmanPosition(), legals, kind='manhattan')


        print(legals, len(legals))
        legal = randint(0, len(legals) - 1)
        print(legal)
        return legal

    def get_distances(self, posFood, posPacman, s, kind='euclidean'):
        from scipy.spatial import distance
        dist = []
        print("actualPacmanPos -> ",posPacman)

        a, b = posPacman
        for i in s:
            if i == 'North':
                posPacman = [a + 1, b]
            if i == 'South':
                posPacman = [a - 1, b]
            if i == 'East':
                posPacman = [a, b + 1]
            if i == 'West':
                posPacman = [a, b - 1]

            # print("the future {} position ".format(i), posPacman)

            if kind == 'euclidean':
                for i in posFood:
                    dist.append(distance.euclidean(i, posPacman))
            elif kind == 'manhattan':
                dist.append([distance.cityblock(i, posPacman) for i in posFood])
            # eu = [distance.euclidean(i, posPacman) for i in posFood]
            # print(dist)
            # print(eu)


        return dist
