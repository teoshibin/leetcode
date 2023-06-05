
from core import AbstractSolution as AS
from core import AbstractTest as AT


class Solution1(AS):
    def solve(self, key: str, message: str) -> str:
        dict = {' ': ' '}
        count = ord('a')
        for k in key:
            if k not in dict:
                dict[k] = chr(count) 
                count += 1
        return "".join([dict[s] for s in message])

    def run(self):
        return self.solve("eljuxhpwnyrdgtqkviszcfmabo","zwx hnfx lqantp mnoeius ycgk vcnjrdb")


class Test(AT):

    def test_case1(self):
        key = "the quick brown fox jumps over the lazy dog"
        message = "vkbs bs t suepuv"
        expected = "this is a secret"
        self.run_assert(self.assertEqual, (key,message), expected)

    def test_case2(self):
        key = "eljuxhpwnyrdgtqkviszcfmabo"
        message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
        expected = "the five boxing wizards jump quickly"
        self.run_assert(self.assertEqual, (key,message), expected)
