import unittest
import importlib
import argparse
import os

from core.AbstractSolution import AbstractSolution

PROBLEMS_DIR = "problems"
TEMPLATE_FILE = os.path.join("core","template.py")


def create_problem_file(problem_number, custom_name=""):
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
    

def problem_module(problem_number: int):
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


def run_test(problem_number, solution_number=None):

    try:
        module = importlib.import_module(problem_module(problem_number))

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

    try:
        # Dynamically import the module
        module = importlib.import_module(problem_module(problem_number))

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
    parser.add_argument('-n', '--name', type=str,
                        help='Specify a custom name for a new problem file.')

    args = parser.parse_args()

    if args.test or args.test == 0:
        run_test(args.test, args.solution)
    elif args.run:
        run_solution(args.run, args.solution)
    elif args.create:
        create_problem_file(args.create, args.name)
        print(f"Problem {args.create} has been created.")
    else:
        print("No problem number provided.")


# Main method
if __name__ == "__main__":
    main()
