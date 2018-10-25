from pacman_module.game import Agent
from pacman_module.pacman import Directions
from random import randint
from pacman_module.util import PriorityQueue
from statistics import mean



class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        self.path = None

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
        legals = state.getLegalActions()
        legals.remove(Directions.STOP)
        action = self._get_action(state)
        print(state.generatePacmanSuccessors()[0][0].getScore())
        food = state.getFood()
        if True in food:
            print("ok")
        
        return action
    def _get_action(self, state):
        if self.path == None:
            self.path = self.astar(state, self.manhattanMean)
        move = self.path[0]
        self.path.pop(0)
        return move

    def astar(self, start, heuristic):
        explored = []
        fringe = PriorityQueue()
        fringe.push((start, []),0)

        while True:
            node = fringe.pop()
            cost, state, path = node[0], node[1][0], node[1][1]
            pacmanState = (state.getPacmanPosition(), state.getFood())

            if pacmanState not in explored:
                explored.append(pacmanState)
                for successor, move in state.generatePacmanSuccessors():
                    # Testing if goal state:
                    goalState = True
                    for i in successor.getFood():
                        for j in i:
                            if j: # not goal state, keep expanding
                                goalState = False
                    if goalState:
                        return path + [move]
                    else:
                        goals = successor.getFood().asList()
                        fringe.push((successor, path+[move]),len(path)+1+heuristic(successor.getPacmanPosition(),goals))

    def manhattan(self, position, goals):
        distances = []
        for goal in goals:
            distances.append(abs(position[0] - goal[0]) + abs(position[1] - goal[1]))
        return min(distances)

    def manhattanMean(self, position, goals):
        distances = []
        for goal in goals:
            distances.append(abs(position[0] - goal[0]) + abs(position[1] - goal[1]))
        return mean(distances)