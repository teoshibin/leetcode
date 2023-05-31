import unittest
import importlib
import argparse
import os
import json

from AbstractSolution import AbstractSolution

HISTORY_FILE = "history.json"
PROBLEMS_DIR = "problems"
TEMPLATE_FILE = "template.py"  # This is the template file you should create


def create_problem_file(problem_number):
    template = ""
    with open(TEMPLATE_FILE, "r") as file:
        template = file.read()

    with open(f"{PROBLEMS_DIR}/problem_{problem_number}.py", "w") as file:
        file.write(template)


# def update_history(problem_number):
#     with open(HISTORY_FILE, "w") as file:
#         json.dump({"last_problem": problem_number}, file)


# def get_last_problem():
#     if os.path.exists(HISTORY_FILE):
#         with open(HISTORY_FILE, "r") as file:
#             data = json.load(file)
#             return data.get("last_problem")
#     return None


def run_test(problem_number, solution_number=None):
    problem_module = f"{PROBLEMS_DIR}.problem_{problem_number}"

    try:
        module = importlib.import_module(problem_module)

        test_class = getattr(module, "TestProblem")

        # Set the solution_number class variable
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
            solution_classes = [cls for cls in solution_classes if cls.number == solution_number] # type: ignore

        for solution_class in solution_classes:
            solution = solution_class()
            solution.run()

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
    # parser.add_argument('-u', '--update', type=int,
    #                     help='Update the history to specific problem number.')

    args = parser.parse_args()

    if args.test:
        run_test(args.test, args.solution)
        # update_history(args.test)
    elif args.run:
        run_solution(args.run, args.solution)
        # update_history(args.run)
    elif args.create:
        create_problem_file(args.create)
        print(f"Problem {args.create} has been created.")
    # elif args.update:
        # update_history(args.update)
        # print(f"History updated to number {args.update}.")
    else:
        # last_problem = get_last_problem()
        # if last_problem:
        #     print(f"Running last executed problem: {last_problem}")
        #     run_test(last_problem)
        # else:
        #     print("No problem number provided and history not found.")
        print("No problem number provided.")


# Main method
if __name__ == "__main__":
    main()
