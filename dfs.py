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

        action = legals[randint(0, len(legals) - 1)]
        print(action)

        return action

