
import unittest
import inspect

from .logger import Logger


class AbstractTest(unittest.TestCase):
    solution_classes = []

    def run_assert(self, assert_func, args, expected_output, **kwargs):
        """Run an assert function for each solution and add the solution number to the error message."""
        logger = Logger.getInstance()
        errors = [] # temporily store raised error to prevent loop interuption when exception occur
        calling_function_name = inspect.stack()[1][3]
        logger.log(calling_function_name + ":")
        for solution_class in self.solution_classes:
            solution = solution_class()
            result = solution.solve(*args)
            try:
                assert_func(result, expected_output, **kwargs)
                logger.log(f"  Passed: {solution.__class__.__name__}")
            except AssertionError as e:
                error_message = f"  Failed: {solution.__class__.__name__} - {e.args[0]}"
                e.args = (error_message,)
                logger.log(error_message)
                errors.append(e)
        if errors:
            raise AssertionError("\n".join(str(e) for e in errors))


    @classmethod
    def tearDownClass(cls):
        print()
        print("----------------------------------------------------------------------")
        logger = Logger.getInstance()
        logger.print_logs()