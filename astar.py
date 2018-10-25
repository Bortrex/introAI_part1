# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from pacman_module.util import PriorityQueue, manhattanDistance
from scipy.spatial import distance
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
        self.posFood = []

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

        if self.path == None:
            self.path = self.astar(state)
        moveTo = self.path[0]
        # print(move)
        self.path.pop(0)

        return moveTo

    def astar(self, currentPos):

        visited = []
        fringe = PriorityQueue()

        fringe.push((currentPos, []), 0)
        while not fringe.isEmpty():
            node = fringe.pop()
            # print("node -> ", node)
            depth, successorPos, path = node[0], node[1][0], node[1][1]
            # print()
            # print(path)
            # print(actualPos.generatePacmanSuccessors())
            successorPacmanState = (successorPos.getPacmanPosition(), successorPos.getFood())
            if successorPacmanState not in visited:
                visited.append(successorPacmanState)

                for successor, direction in successorPos.generatePacmanSuccessors():
                    minDist = self.get_distance(successor)
                    cost = 1
                    if minDist < depth:
                        cost = -1
                    goal = True
                    for foods in successor.getFood():
                        for isGoalState in foods:
                            if isGoalState:
                                goal = False
                    if goal:
                        return path + [direction]
                    else:
                        depth = cost + len(path) + self.get_distance(successor)
                        fringe.push((successor, path+[direction]), depth) # depth -1 for dfs| depth for bfs | depth + 1 for ucs

    def get_distance(self, successor):
        successorPos = successor.getPacmanPosition()
        successorFood = successor.getFood().asList()
        dist = []

        for i in successorFood:
            dist.append(manhattanDistance(successorPos, i))
            # dist.append(distance.correlation(successorPos, i))
            # dist.append(distance.cosine(successorPos, i))

        # return min(dist or [0])
        return mean(dist or [0])


