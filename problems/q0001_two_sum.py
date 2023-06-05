
from typing import List
from core import AbstractSolution as AS
from core import AbstractTest as AT


class Solution1(AS):
    def solve(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            if n in dict:
                return [dict[n], i]
            dict[target - n] = i
        return []

    def run(self):
        return self.solve([2,7,11,15], 9)

class Test(AT):
    def test_case1(self):
        nums = [2,7,11,15]
        target = 9
        output = [0,1]
        self.run_assert(self.assertEqual, (nums,target), output)

    def test_case2(self):
        nums = [3,2,4]
        target = 6
        output = [1,2]
        self.run_assert(self.assertEqual, (nums,target), output)

    def test_case3(self):
        nums = [3,3]
        target = 6
        output = [0,1]
        self.run_assert(self.assertEqual, (nums,target), output)