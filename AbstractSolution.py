
from abc import ABCMeta, abstractmethod


class SolutionMeta(ABCMeta):
    solutions = []
    counter = 1

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if bases:  # This condition is to skip the AbstractSolution class itself
            cls.number = SolutionMeta.counter
            SolutionMeta.counter += 1
            SolutionMeta.solutions.append(cls)


class AbstractSolution(metaclass=SolutionMeta):
    solution_number = None

    @abstractmethod
    def solve(self, input):
        """
        The method that solves the problem.
        All solutions must implement this method.

        Returns:
            Any: solution result
        """
        pass

    @abstractmethod
    def run(self):
        """ 
        The method to run the solution. 
        Used for debugging solution. 
        All solutions must implement this method.

        Returns:
            Any: returned value will be printed
        """
        pass
