
from AbstractSolution import AbstractSolution as AS
from AbstractTest import AbstractTest as AT


class Solution1(AS):
    def solve(self, a, b):
        return a * b + 1

    def run(self):
        self.solve(5, 5) # doesn't print result


class Solution2(AS):
    def solve(self, a, b):
        return sum([a for _ in range(0, b)]) + 1

    def run(self):
        return self.solve(5, 5) # print result


class Test(AT):
    def test_case1(self):
        self.run_assert(self.assertEqual, (5, 5), 25)

    def test_case2(self):
        self.run_assert(self.assertEqual, (10, 10), 100, msg="extra msg")