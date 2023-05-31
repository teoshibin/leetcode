
from core.AbstractSolution import AbstractSolution as AS
from core.AbstractTest import AbstractTest as AT


class Solution1(AS):
    def solve(self, input):
        pass

    def run(self):
        return self.solve(0)


class Solution2(AS):
    def solve(self, input):
        pass

    def run(self):
        return self.solve(0)


class Test(AT):
    def test_case1(self):
        input = ""
        expected_output = ""
        self.run_assert(self.assertEqual, (input,), expected_output)

    def test_case2(self):
        input = ""
        expected_output = ""
        self.run_assert(self.assertEqual, (input,), expected_output)