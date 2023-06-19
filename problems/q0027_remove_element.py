
from typing import List
from core import AbstractSolution as AS
from core import AbstractTest as AT


class Solution1(AS):
    def solve(self, nums: List[int], val: int) -> List[int]:
        # dynamic array
        while val in nums:
            nums.remove(val)
        return nums

    def run(self):
        input = ([0,1,2,2,3,0,4,2], 2)
        # [0,1,4,0,3]
        return self.solve(*input)


class Solution2(AS):
    def solve(self, nums: List[int], val: int) -> List[int]:
        c = 0
        for n in nums:
            if n != val:
                nums[c] = n
                c += 1
        return nums

    def run(self):
        input = ([0,1,2,2,3,0,4,2], 2)
        # [0,1,4,0,3]
        return self.solve(*input)

class Test(AT):
    def test_case1(self):
        pass
