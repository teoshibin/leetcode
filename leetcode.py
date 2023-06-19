import argparse

from core import ProblemHandler
from core import HistoryHandler


def main():

    problem_handler = ProblemHandler()
    history_handler = HistoryHandler()

    parser = argparse.ArgumentParser(description='Run or create LeetCode problem tests.')
    
    parser.add_argument('-t', '--test', type=int, help='Test a specific problem number.')
    parser.add_argument('-r', '--run', type=int, help='Run a specific problem number.')
    parser.add_argument('-s', '--solution', type=int, help='Specify a solution number.')
    parser.add_argument('-c', '--create', type=int, help='Create a new problem file from template.')
    parser.add_argument('-n', '--name', type=str, help='Specify a custom name for a new problem file.')

    args = parser.parse_args()

    if args.run is None and args.test is None and args.create is None:
        args = argparse.Namespace()
        if history_handler.last_type == "t":
            args.test = history_handler.last_problem
            args.run = None
        else:
            args.run = history_handler.last_problem
            args.test = None
        args.solution = history_handler.last_solution
        args.create = None
        args.name = ""

        print("No valid problem number provided, using history.")
        print(f"./leetcode.py -{history_handler.last_type} {history_handler.last_problem}" + 
              (f" -s {args.solution}" if args.solution else "") + "\n")

    else:
        type = 't' if args.test is not None else 'r'
        problem = args.test if args.test != None else args.run
        history_handler.update(type, problem, args.solution)

    if args.test or args.test == 0:
        problem_handler.run_test(args.test, args.solution)
    elif args.run or args.run == 0:
        problem_handler.run_solution(args.run, args.solution)
    elif args.create:
        problem_handler.create_problem_file(args.create, args.name)
        print(f"Problem {args.create} has been created.")
    else:
        print("No problem number provided.")

if __name__ == "__main__":
    main()
