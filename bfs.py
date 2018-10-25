# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from pacman_module.util import PriorityQueue


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
        # return Directions.STOP
        legals = state.getLegalActions()
        legals.remove(Directions.STOP)

        if self.path == None:
            self.path = self.bfs(state)
        moveTo = self.path[0]
        self.path.pop(0)

        return moveTo

    def get_legals(self, s, currentPos):

        movements = []
        a, b = currentPos
        walls = s.getWalls()
        # print(walls[a][b])

        if not walls[a + 1][b]:  # for East move
            movements.append((a + 1, b))
        if not walls[a - 1][b]:  # for West move
            movements.append((a - 1, b))
        if not walls[a][b + 1]:  # for North move
            movements.append((a, b + 1))
        if not walls[a][b - 1]:  # for South move
            movements.append((a, b - 1))

        return movements

    def bfs(self, currentPos):

        visited = []
        fringe = PriorityQueue()

        fringe.push((currentPos, []), 0)

        while not fringe.isEmpty():
            node = fringe.pop()
            print("node -> ", node)
            depth, successorPos, path = node[0], node[1][0], node[1][1]
            # print()
            # print(path)
            # print(actualPos.generatePacmanSuccessors())

            successorPacmanState = (successorPos.getPacmanPosition(), successorPos.getFood())
            if successorPacmanState not in visited:
                visited.append(successorPacmanState)

                for successor, direction in successorPos.generatePacmanSuccessors():
                    # print(direction)
                    goal = True
                    for directions in successor.getFood():
                        for isGoalState in directions:
                            if isGoalState:
                                goal = False
                    if goal:
                        return path + [direction]
                    else:
                        depth = len(path)
                        fringe.push((successor, path + [direction]), depth)  # depth -1 for dfs| depth for bfs | depth + 1 for ucs
