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
        self.SAMPLE_HELL_TRIANGLE = HellTriangle(self.SAMPLE_TRIANGLE)

    def test__init__without_pass_triangle__should_throw(self):
        assert_that(HellTriangle).raises(Exception).when_called_with()

    def test__init__with_sample_triangle__should_have_sample_triangle(self):
        target = self.SAMPLE_HELL_TRIANGLE.triangle
        assert_that(target).is_equal_to(self.SAMPLE_TRIANGLE)

    def test__find_maximum_total__a_triangle_of_numbers__return_the_maximum_total_from_top_to_bottom(self):
        target = self.SAMPLE_HELL_TRIANGLE
        assert_that(target.find_maximum_total()).is_equal_to(self.SAMPLE_TRIANGLE_MAXIMUM)

    def test__get_two_nearest_x_indexes__sample_triangle_first_line__return_0_and_1(self):
        target = self.SAMPLE_HELL_TRIANGLE
        assert_that(target.get_two_nearest_x_indexes(0, 0)).is_equal_to({"left":0, "right":1})

    def test__get_two_nearest_x_indexes__sample_triangle_first_column__return_0_and_1(self):
        target = self.SAMPLE_HELL_TRIANGLE
        assert_that(target.get_two_nearest_x_indexes(0, 1)).is_equal_to({"left":0, "right":1})

    def test__get_two_nearest_x_indexes__sample_triangle_middle_column__return_1_and_2(self):
        target = self.SAMPLE_HELL_TRIANGLE
        assert_that(target.get_two_nearest_x_indexes(1, 2)).is_equal_to({"left":1, "right":2})

    def test__get_two_nearest_x_indexes__sample_triangle_last_column__return_2_and_3(self):
        target = self.SAMPLE_HELL_TRIANGLE
        assert_that(target.get_two_nearest_x_indexes(2, 2)).is_equal_to({"left":2, "right":3})
    
    def test__get_two_nearest_x_indexes__sample_triangle_at_last_line__return_none(self):
        target = self.SAMPLE_HELL_TRIANGLE
        assert_that(target.get_two_nearest_x_indexes(0, 3)).is_none()

unittest.main()