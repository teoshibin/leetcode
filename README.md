
# Leetcode Framework for Python

This is a simple framework for test running leetcode locally. Allowing solving, running and testing.

## Template Example

Here we have an example solving multiplication, it can be found in  [problems/q0000_demo.py](problems/q0000_demo.py).
The idea is that each problem will have multiple solutions with the same test case and each test case can test one or more solutions.

> Note that class name `Test` shouldn't be changed.   
> However, solution class name can be change e.g. `DP(AS)`, this allows naming the solution.   
> Additionally, `Test` identify Solution based on the order that they are declared. Thus, the example below, Solution1 is 1, Solution2 is 2, this is useful to know when specifying solution number when using cli.

```python

from  core.AbstractSolution import AbstractSolution as AS
from core.AbstractTest import AbstractTest as AT


class Solution1(AS):
    def solve(self, a, b):
        return a * b

    def run(self):
        self.solve(5, 5) # doesn't print result
        print("hello world")

class Solution2(AS):
    def solve(self, a, b):
        return sum([a for _ in range(0, b)])

    def run(self):
        return self.solve(5, 5) # print result


class Test(AT):
    def test_case1(self):
        self.run_assert(self.assertEqual, (5, 5), 25)

    def test_case2(self):
        self.run_assert(self.assertEqual, (10, 10), 100, msg="extra msg")

```

## Commands

```bash
py ./leetcode.py -c 100                 # create q100.py
py ./leetcode.py -c 100 -n same_tree    # create q100_same_tree.py
py ./leetcode.py -r 100                 # run all solutions for problem 100
py ./leetcode.py -r 100 -s 2            # run solution 2 for problem 100
py ./leetcode.py -t 100                 # unit test all solutions for problem 100
py ./leetcode.py -t 100 -s 1            # unit test solution 1 for problem 100

~> py ./leetcode.py -h
usage: leetcode.py [-h] [-t TEST] [-r RUN] [-s SOLUTION] [-c CREATE] [-n NAME]

Run or create LeetCode problem tests.

options:
  -h, --help            show this help message and exit
  -t TEST, --test TEST  Test a specific problem number.
  -r RUN, --run RUN     Run a specific problem number.
  -s SOLUTION, --solution SOLUTION
                        Specify a solution number.
  -c CREATE, --create CREATE
                        Create a new problem file from template.
  -n NAME, --name NAME  Specify a custom name for a new problem file.
```

# Example Test

```bash
~> py ./leetcode.py -t 0
No solution number given, testing all solutions

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
Ran 2 tests in 0.005s

OK
```

> It is highly possible that some input or output scenario aren't handled, as there are thousands of questions and I'm not working in meta so I won't bother adding support until I encounter them myself.
