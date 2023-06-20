
from math import inf
from typing import List
from core import AbstractSolution as AS
from core import AbstractTest as AT


# TODO more solution
class Solution1(AS):
    def solve(self, coordinates: List[List[int]]) -> bool:
        his_m = None
        for i in range(len(coordinates)-1):
            x_diff = coordinates[i+1][0] - coordinates[i][0]
            y_diff = coordinates[i+1][1] - coordinates[i][1]
            if x_diff == 0:
                m = inf
            else:
                m = y_diff / x_diff
            if his_m == None:
                his_m = m
            elif his_m != m:
                return False
        return True

    def run(self):
        return self.solve([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])


class Test(AT):
    def test_case1(self):
        input = [[0,0],[0,1],[0,-1]]
        expected_output = True
        self.run_assert(self.assertEqual, (input,), expected_output)

    def test_case2(self):
        input = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
        expected_output = True
        self.run_assert(self.assertEqual, (input,), expected_output)