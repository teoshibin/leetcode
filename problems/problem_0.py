from AbstractSolution import AbstractSolution
from AbstractTestProblem import AbstractTestProblem

class Solution1(AbstractSolution):
    number = AbstractSolution.next_solution()

    def solve(self, input):
        return 1
    
    def run(self):
        print("hello" + str(self.number))


class Solution2(AbstractSolution):
    number = AbstractSolution.next_solution()

    def solve(self, input):
        return 2
    
    def run(self):
        print("hello" + str(self.number))


class TestProblem(AbstractTestProblem):
    def get_solution_classes(self):
        return [Solution1, Solution2]

    def test_case1(self):
        input = ""
        expected_output = 3
        self.run_test_case(input, expected_output)

    def test_case2(self):
        input = ""
        expected_output = 2
        self.run_test_case(input, expected_output)

