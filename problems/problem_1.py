from AbstractSolution import AbstractSolution
from AbstractTestProblem import AbstractTestProblem

class Solution1(AbstractSolution):
    number = AbstractSolution.next_solution()

    def solve(self, input):
        pass
    
    def run(self):
        pass


class Solution2(AbstractSolution):
    number = AbstractSolution.next_solution()

    def solve(self, input):
        pass
    
    def run(self):
        pass


class TestProblem(AbstractTestProblem):
    def get_solution_classes(self):
        return [Solution1, Solution2]

    def test_case1(self):
        input = ""
        expected_output = ""
        self.run_test_case(input, expected_output)


