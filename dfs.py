# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
import numpy as np
import random
from random import randint
from queue import PriorityQueue


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        self.posFood = []
        self.queueDirections = list()

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
        # print(state.generatePacmanSuccessors())

        currentFood = list(state.getFood())

        print("\n\n# of Food -> ", state.getNumFood())

        if not self.posFood:
            for i in range(len(currentFood)):  # columns
                for j in range(len(currentFood[0])):  # rows
                    if currentFood[i][j] == True:
                        self.posFood.append((i, j))

        if not self.queueDirections:#.empty():
            posPacman = state.getPacmanPosition()
            goal = self.posFood[0]
            # print(goal)
            # Computation of the path to the goal
            dfs = self.dfs(state, goal, posPacman)
            path = self.graph(goal, dfs, state)
            # Enter the path to follow
            for i in range(len(path)):
                self.queueDirections.append(path[i])

            # self.queueDirections.append([path[i] for i in range(len(path))])
            print("pathlist ",self.queueDirections)
        else:
            ss = self.queueDirections.pop()
            print("ss ",ss)#[0], ss[1])
            return Directions.WEST


        # action = legals[randint(0, len(legals) - 1)]
        # print(action)

        return Directions.STOP

    def get_legals(self, s, currentPos):

        movements = []
        a, b = currentPos
        walls = s.getWalls()
        # print(walls[a][b])
        # for i in legals:
        #     if i == 'North':
        #         movements.append((a + 1, b))
        #     if i == 'South':
        #         movements.append((a - 1, b))
        #     if i == 'East':
        #         movements.append((a, b + 1))
        #     if i == 'West':
        #         movements.append((a, b - 1))

        if not walls[a + 1][b]:
            movements.append((a + 1, b))
        if not  walls[a - 1][b]:
            movements.append((a - 1, b))
        if not walls[a][b + 1]:
            movements.append((a, b + 1))
        if not  walls[a][b-1]:
            movements.append((a, b - 1))

        return movements

    def dfs(self, state, posFood, posPacman, ):

        previous_state = {}
        visited = []
        fringe = PriorityQueue()

        fringe.put((0, posPacman, visited))
        # previous_state[posPacman] = None

        # print(fringe.get())
        # print(state.getLegalActions())
        # print(posFood)
        while not fringe.empty():

            depth, actualPos, visited = fringe.get()
            # print("actual->", actualPos)
            if actualPos == posFood:#state.isWin():
                print("isWin", previous_state)
                return previous_state


            # Add to our list of explored nodes
            visited = visited + [actualPos]
            legal_moves = self.get_legals(state, actualPos)

            # print(len(legal_moves), legal_moves)
            for next_mov in legal_moves:
                # print(next_mov)
                if next_mov not in previous_state and next_mov not in visited :
                    # if next_mov == posFood:
                    #     return previous_state


                    previous_state[next_mov] = actualPos
                    depth_node = len(previous_state)
                    # print(next_mov, type(next_mov))

                    fringe.put((-depth_node, next_mov, visited + [next_mov]))



    def graph(self, goal, previous_State, state):

        x, y = state.getPacmanPosition()
        current = goal
        path = [goal]
        while not(current[0] == x and current[1] == y):
            current = previous_State[current]
            path.append(current)

        print(path)
        return path
