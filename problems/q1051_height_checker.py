
from typing import List
from core import AbstractSolution as AS
from core import AbstractTest as AT


class Solution1(AS):
    def solve(self, heights: List[int]) -> int:
        hs = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if hs[i] != heights[i]:
                count += 1
        return count

    def run(self):
        return self.solve([1,1,4,2,1,3])


class Test(AT):
    def test_case1(self):
        input = ""
        expected_output = ""
        self.run_assert(self.assertEqual, (input,), expected_output)
