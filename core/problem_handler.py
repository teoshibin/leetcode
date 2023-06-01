
import unittest
import importlib
import os

from core.solution_manager import SolutionManager

from .abstract_solution import AbstractSolution


PROBLEMS_DIR = "problems"
TEMPLATE_FILE = os.path.join("core","template.py")


class ProblemHandler:
    def __init__(self):
        self.solution_manager = SolutionManager()
        pass


    def _problem_module(self, problem_number: int) -> str:
        """
        Get the module name corresponding to a problem number.

        Args:
            problem_number (int): The problem number

        Returns:
            str: The module name

        Raises:
            FileNotFoundError: If the problem module is not found
        """
        padded_problem_number = str(problem_number).zfill(4)
        problem_file = None

        # Search for the file in the problems directory
        for filename in os.listdir(PROBLEMS_DIR):
            if filename.startswith(f"q{padded_problem_number}"):
                problem_file = filename.replace(".py", "")
                break

        if problem_file is None:
            raise FileNotFoundError(f"Problem {problem_number} not found")

        return f"{PROBLEMS_DIR}.{problem_file}"


    def create_problem_file(self, problem_number: int, custom_name: str = "") -> None:
        """
        Create a new problem file from a template.

        Args:
            problem_number (int): The problem number
            custom_name (str, optional): A custom name for the problem file. Defaults to "".

        Raises:
            FileExistsError: If the problem file already exists
        """
        template = ""
        with open(TEMPLATE_FILE, "r") as file:
            template = file.read()

        padded_problem_number = str(problem_number).zfill(4)
        appended_name = f"_{custom_name}" if custom_name else ""
        filename = os.path.join(PROBLEMS_DIR, f"q{padded_problem_number}{appended_name}.py")

        if os.path.exists(filename):
            raise FileExistsError(f"The file {filename} already exists")
        else:
            with open(filename, "w") as file:
                file.write(template)


    def run_test(self, problem_number: int, solution_number: int | None = None) -> unittest.TestResult | None:
        """
        Run a test for a problem and return the result.

        Args:
            problem_number (int): The problem number
            solution_number (int, optional): The solution number to test. If not provided, all solutions are tested.

        Returns:
            unittest.TestResult: The test result

        Raises:
            ModuleNotFoundError: If the problem module is not found
        """
        try:
            module = importlib.import_module(self._problem_module(problem_number))
            test_class = getattr(module, "Test")

            # Set the solution_number class variable
            if solution_number == None:
                print("No solution number given, testing all solutions\n")
            test_class.solution_number = solution_number

            # Run the tests
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
            # TODO(return result)
            # result = unittest.TestResult()
            # suite.run(result)
            # return result
            unittest.TextTestRunner().run(suite)
        except ModuleNotFoundError:
            print(f"Problem {problem_number} not found")


    def run_solution(self, problem_number: int, solution_number: int | None = None) -> None:
        """
        Run a solution for a problem and print the result.

        Args:
            problem_number (int): The problem number
            solution_number (int, optional): The solution number to run. If not provided, all solutions are run.

        Raises:
            ModuleNotFoundError: If the problem module is not found
        """
        try:
            # Dynamically import the module
            module = importlib.import_module(self._problem_module(problem_number))

            # Get the solution classes
            solution_classes = [cls for cls in module.__dict__.values()
                                if isinstance(cls, type)
                                and issubclass(cls, AbstractSolution)
                                and cls.__module__ == module.__name__]

            if solution_number is not None:
                solution_classes = [cls for cls in solution_classes
                                    if cls.number == solution_number]

            for solution_class in solution_classes:
                solution = solution_class()
                out = solution.run()
                if out:
                    print(solution_class.__name__ + ":")
                    print(out)

        except ModuleNotFoundError:
            print(f"Problem {problem_number} not found")
