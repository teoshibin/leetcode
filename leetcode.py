import argparse

from core import ProblemHandler


def main():
    parser = argparse.ArgumentParser(description='Run or create LeetCode problem tests.')
    
    parser.add_argument('-t', '--test', type=int, help='Test a specific problem number.')
    parser.add_argument('-r', '--run', type=int, help='Run a specific problem number.')
    parser.add_argument('-s', '--solution', type=int, help='Specify a solution number.')
    parser.add_argument('-c', '--create', type=int, help='Create a new problem file from template.')
    parser.add_argument('-n', '--name', type=str, help='Specify a custom name for a new problem file.')

    args = parser.parse_args()

    problem_handler = ProblemHandler()

    # TODO(invalid argument check)
    if args.test or args.test == 0:
        problem_handler.run_test(args.test, args.solution)
    elif args.run or args.run == 0:
        problem_handler.run_solution(args.run, args.solution)
    elif args.create:
        problem_handler.create_problem_file(args.create, args.name)
        print(f"Problem {args.create} has been created.")
    else:
        print("No problem number provided.")

# Main method
if __name__ == "__main__":
    main()
