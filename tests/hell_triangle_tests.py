import os
import sys
import unittest
from assertpy import assert_that
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib import HellTriangle

class HellTriangleTests(unittest.TestCase):
    def setUp(self):
        self.SAMPLE_TRIANGLE = [[6],[3,5],[9,7,1],[4,6,8,4]]
        self.SAMPLE_TRIANGLE_MAXIMUM = 26

    def test__init__without_pass_triangle__should_throw(self):
        assert_that(HellTriangle).raises(Exception).when_called_with()

    def test__init__with_sample_triangle__should_have_sample_triangle(self):
        target = HellTriangle(self.SAMPLE_TRIANGLE).triangle
        assert_that(target).is_equal_to(self.SAMPLE_TRIANGLE)

    def test__find_maximum_total__a_triangle_of_numbers__return_the_maximum_total_from_top_to_bottom(self):
        target = HellTriangle(self.SAMPLE_TRIANGLE)
        assert_that(target.find_maximum_total()).is_equal_to(self.SAMPLE_TRIANGLE_MAXIMUM)

unittest.main()