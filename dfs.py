# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
import numpy as np
import random
from random import randint
from queue import PriorityQueue
from scipy.spatial import distance

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

        if not self.queueDirections:  # isempty():
            posPacman = state.getPacmanPosition()
            goal = []#self.posFood[0]
            higher_dist = 0

            # print(len(self.posFood))
            # for i in range(len(self.posFood)):
            #     # TODO: here we can implement an euclidean function dist to select the shortest one
            #     food_distance = distance.euclidean(posPacman, self.posFood[i])
            #     # print(food_distance)
            #     if food_distance > higher_dist:
            #
            #         goal = self.posFood[i]
            #         print(higher_dist)
            #         higher_dist = food_distance

            goal = self.posFood[self.get_nearest_goal(posPacman, "manhattan")]
            print(goal)
            # Searching of the path to the goal
            dfs = self.dfs(state, goal, posPacman)

            x, y = posPacman
            actual_goal = goal
            path = [goal]
            while not (actual_goal[0] == x and actual_goal[1] == y):
                actual_goal = dfs[actual_goal]
                path.append(actual_goal)

            print("is a Win path -", path)
            # Enter the path to follow
            for i in range(len(path)):
                self.queueDirections.append(path[i])

            # self.queueDirections.append([path[i] for i in range(len(path))])
        else:
            next_path_move = self.queueDirections.pop() # pop() for LIFO, pop(0) for FIFO
            x_new, y_new = next_path_move
            print("next Move - ", next_path_move)  # [0], ss[1])
            actual_posPacman = state.getPacmanPosition()
            actual_posFood = state.getFood()

            if tuple(np.subtract(actual_posPacman, (1,0))) == next_path_move:
                if actual_posFood[x_new][y_new]:
                    self.posFood.remove((x_new,y_new))
                return Directions.WEST
            elif tuple(np.subtract(actual_posPacman, (0, 1))) == next_path_move:
                if actual_posFood[x_new][y_new]:
                    self.posFood.remove((x_new,y_new))
                return Directions.SOUTH
            elif tuple(np.add(actual_posPacman, (0, 1))) == next_path_move:
                if actual_posFood[x_new][y_new]:
                    self.posFood.remove((x_new,y_new))
                return Directions.NORTH
            elif tuple(np.add(actual_posPacman, (1, 0))) == next_path_move:
                if actual_posFood[x_new][y_new]:
                    self.posFood.remove((x_new,y_new))
                return Directions.EAST
            else: return Directions.STOP


        return Directions.STOP

    def get_legals(self, s, currentPos):

        movements = []
        a, b = currentPos
        walls = s.getWalls()
        # print(walls[a][b])

        if not walls[a + 1][b]: # for East move
            movements.append((a + 1, b))
        if not walls[a - 1][b]: # for West move
            movements.append((a - 1, b))
        if not walls[a][b + 1]: # for North move
            movements.append((a, b + 1))
        if not walls[a][b - 1]: # for South move
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
            # Creation of node
            state.generatePacmanSuccessors()

            # print("actual->", actualPos)
            if actualPos == posFood:  # state.isWin():
                print("is a Win grid", previous_state)
                return previous_state

            # Add to our list of explored nodes
            visited = visited + [actualPos]
            legal_moves = self.get_legals(state, actualPos)

            # print(len(legal_moves), legal_moves)
            for next_mov in legal_moves:
                # print(next_mov)
                if next_mov not in previous_state and next_mov not in visited:
                    # if next_mov == posFood:
                    #     return previous_state

                    previous_state[next_mov] = actualPos
                    depth_node = len(previous_state)
                    # print(next_mov, type(next_mov))

                    fringe.put((-depth_node, next_mov, visited + [next_mov]))

    def get_nearest_goal(self, posPacman, type='euclidean'):
        goals = []
        for i in self.posFood:
            if type == 'euclidean':
                goals.append(distance.euclidean(posPacman, i))
            elif type == 'manhattan':
                goals.append(distance.cityblock(posPacman, i))


        print(goals)
        return goals.index(min(goals))

