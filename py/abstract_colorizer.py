#!/usr/bin/env python
from abc import ABC
from colorization_solver import ColorizationSolver

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


class AbstractColorizer(ABC):
    """
    A class used to represent an abstract colorizer.

    ...

    Attributes
    ----------
    _colorization_solver : ColorizationSolver
        object solving colorization problem

    Methods
    -------
    colorize()
        Abstract method.
        Runs colorization process.
    """

    def __init__(self):
        self._colorization_solver = ColorizationSolver()

    def colorize(self):
        pass
