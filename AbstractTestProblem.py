import unittest
from abc import abstractmethod

class AbstractTestProblem(unittest.TestCase):
    solution_number = None  # Define the solution_number as a class variable

    @abstractmethod
    def get_solution_classes(self):
        """Return a list of solution classes for the problem. This must be overridden by each subclass."""
        pass

    def setUp(self):
        solutions = self.get_solution_classes()
        if self.__class__.solution_number is not None:  # Access it as a class variable
            self.solutions = [solution() for solution in solutions if solution.number == self.__class__.solution_number] # type: ignore
        else:
            self.solutions = [solution() for solution in solutions] # type: ignore

    def run_test_case(self, input, expected_output):
        """Run a test case for all solutions, comparing the output to the expected result."""
        for solution in self.solutions:
            self.assertEqual(solution.solve(input), expected_output)
