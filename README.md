
# LeetCode Framework for Python

This Python-based framework is designed to streamline your experience of solving, running, and testing LeetCode problems locally. It takes the hassle out of running multiple solutions and their corresponding test cases, letting you focus on what matters most: problem-solving.

## Structure of a Problem Solution

Every LeetCode problem is captured in a Python file, following a particular structure. To illustrate, consider the multiplication problem in [problems/q0000_demo.py](problems/q0000_demo.py). Each problem file consists of a `Test` class that encompasses multiple solutions and their test cases.

Take note that the `Test` class name must remain constant, whereas solution class names (for instance, `MySolution(AS)`) can vary, facilitating descriptive solution naming. The `Test` class identifies solutions by their order of declaration. Consequently, in the example below, Solution1 equates to 1, Solution2 to 2, and so forth. This is crucial when specifying the solution number in the command-line interface (CLI).

```python
from  core.AbstractSolution import AbstractSolution as AS
from core.AbstractTest import AbstractTest as AT


class Solution1(AS):
    def solve(self, a, b):
        return a * b

    def run(self):
        self.solve(5, 5)
        print("hello world")

class Solution2(AS):
    def solve(self, a, b):
        return sum([a for _ in range(0, b)])

    def run(self):
        return self.solve(5, 5) # returned results are printed


class Test(AT):
    def test_case1(self):
        self.run_assert(self.assertEqual, (5, 5), 25)

    def test_case2(self):
        self.run_assert(self.assertEqual, (10, 10), 100, msg="extra msg")
```

## CLI (Command Line Interface) Usage

You can execute several commands in the terminal:

```bash
py ./leetcode.py -c 100                 # creates q100.py
py ./leetcode.py -c 100 -n same_tree    # creates q100_same_tree.py
py ./leetcode.py -r 100                 # runs all solutions for problem 100
py ./leetcode.py -r 100 -s 2            # runs solution 2 for problem 100
py ./leetcode.py -t 100                 # performs unit testing on all solutions for problem 100
py ./leetcode.py -t 100 -s 1            # performs unit testing on solution 1 for problem 100
py ./leetcode.py                        # executes the last executed command
```

For a helpful guide on using these commands, employ the `-h` flag:

```bash
py ./leetcode.py -h
```

## History and Default Execution

The framework automatically records the last problem and solution number you executed (either `run` or `test`). This data is saved in a `history.json` file.

If you run the command without any arguments, the system will default to executing the last problem and solution specified in the history file. If no specific solution number is available, it will execute all solutions for the last problem.

## Debugging

`.vscode` launch options are pre-configured to use `leetcode.py` as the entry point. So, simply set your breakpoints in your solver and press `F5` to start debugging.

## Test Execution Examples

Here are some examples of how to execute tests:

```bash
~> py ./leetcode.py -t 0
No solution number provided, testing all solutions

..
----------------------------------------------------------------------
test_case1:
  Passed: Solution1
  Passed: Solution2
test_case2:
  Passed: Solution1
  Passed: Solution2

----------------------------------------------------------------------
Ran 2 tests in 0.008s

OK
```

```bash
~> py ./leetcode.py -t 0 -s 2
..
----------------------------------------------------------------------
test_case1:
  Passed: Solution2
test_case2:
  Passed: Solution2
----------------------------------------------------------------------
```

## License

This project is licensed under the terms of the [MIT license](LICENSE).
