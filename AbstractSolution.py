from abc import ABC, abstractmethod

class AbstractSolution(ABC):
    solution_number = 0

    @abstractmethod
    def solve(self, input):
        """The method that solves the problem. All solutions must implement this method."""
        pass

    @abstractmethod
    def run(self):
        """The method to run the solution. All solutions must implement this method."""
        pass

    @classmethod
    def next_solution(cls):
        """Increments the solution number and returns the next solution number."""
        cls.solution_number += 1
        return cls.solution_number