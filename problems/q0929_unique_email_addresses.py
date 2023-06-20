
from typing import List
from core import AbstractSolution as AS
from core import AbstractTest as AT


class Solution1(AS):
    def solve(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            (local_name, domain) = e.split("@")
            local = local_name.split("+")
            name = local[0].replace(".","")
            s.add(f"{name}@{domain}")
        return len(s)

    def run(self):
        return self.solve(["test.email+alex@leetcode.com",
                           "test.e.mail+bob.cathy@leetcode.com",
                           "testemail+david@lee.tcode.com"])


class Test(AT):
    def test_case1(self):
        input = ""
        expected_output = ""
        self.run_assert(self.assertEqual, (input,), expected_output)
