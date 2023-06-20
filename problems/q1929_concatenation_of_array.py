
from typing import List
from core import AbstractSolution as AS
from core import AbstractTest as AT


class Solution1(AS):
    def solve(self, nums: List[int]) -> List[int]:
        return nums + nums

    def run(self):
        return self.solve([1,3,2,1])


class Test(AT):
    def test_case1(self):
        input = ""
        expected_output = ""
        self.run_assert(self.assertEqual, (input,), expected_output)
