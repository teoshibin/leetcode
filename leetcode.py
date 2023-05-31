import unittest
import importlib
import argparse

from AbstractSolution import AbstractSolution

PROBLEMS_DIR = "problems"
TEMPLATE_FILE = "template.py"


def create_problem_file(problem_number):
    template = ""
    with open(TEMPLATE_FILE, "r") as file:
        template = file.read()

    with open(f"{PROBLEMS_DIR}/problem_{problem_number}.py", "w") as file:
        file.write(template)


def run_test(problem_number, solution_number=None):
    problem_module = f"{PROBLEMS_DIR}.problem_{problem_number}"

    try:
        module = importlib.import_module(problem_module)

        test_class = getattr(module, "Test")

        # Set the solution_number class variable
        if solution_number == None:
            print("No solution number given, testing all solutions\n")
        test_class.solution_number = solution_number

        # Run the tests
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
        unittest.TextTestRunner().run(suite)
    except ModuleNotFoundError:
        print(f"Problem {problem_number} not found")


def run_solution(problem_number, solution_number=None):
    problem_module = f"{PROBLEMS_DIR}.problem_{problem_number}"

    try:
        # Dynamically import the module
        module = importlib.import_module(problem_module)

        # Get the solution classes
        solution_classes = [cls for cls in module.__dict__.values() if isinstance(
            cls, type) and issubclass(cls, AbstractSolution) and cls.__module__ == module.__name__]

        if solution_number is not None:
            solution_classes = [
                cls for cls in solution_classes if cls.number == solution_number]  # type: ignore

        for solution_class in solution_classes:
            solution = solution_class()
            out = solution.run()
            if out:
                print(solution_class.__name__ + ":")
                print(out)

    except ModuleNotFoundError:
        print(f"Problem {problem_number} not found")


def main():
    parser = argparse.ArgumentParser(
        description='Run or create LeetCode problem tests.')
    parser.add_argument('-t', '--test', type=int,
                        help='Test a specific problem number.')
    parser.add_argument('-r', '--run', type=int,
                        help='Run a specific problem number.')
    parser.add_argument('-s', '--solution', type=int,
                        help='Specify a solution number.')
    parser.add_argument('-c', '--create', type=int,
                        help='Create a new problem file from template.')

    args = parser.parse_args()

    if args.test or args.test == 0:
        run_test(args.test, args.solution)
    elif args.run:
        run_solution(args.run, args.solution)
    elif args.create:
        create_problem_file(args.create)
        print(f"Problem {args.create} has been created.")
    else:
        print("No problem number provided.")


# Main method
if __name__ == "__main__":
    main()
