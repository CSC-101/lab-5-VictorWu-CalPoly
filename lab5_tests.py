from data import Point, Time
import lab5
import unittest

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.

    # Part 3
    #### Time_Add Tests
    def test_Time_add_1(self):
        time1 = Time(4, 5, 10)
        time2 = Time(6, 7, 60)
        result = lab5.time_add(time1, time2)
        expected = Time(10, 13, 10)
        self.assertEqual(result, expected)

    def test_Time_add_2(self):
        time1 = Time(10, 99, 60)
        time2 = Time(100, 7, 60)
        result = lab5.time_add(time1, time2)
        expected = Time(111, 48, 0)
        self.assertEqual(result, expected)

    # Part 4
    #### Is_Descending Tests
    def test_is_descending_1(self):
        list_1 = [2.2, 5.2, 3.3, 9.9, 1.1]
        result = lab5.is_descending(list_1)
        expected = [9.9, 5.2, 3.3, 2.2, 1.1]
        self.assertEqual(result, expected)

    def test_is_descending_2(self):
        list_1 = [10.1, 2.3, 2.2, 2.1, 2.25]
        result = lab5.is_descending(list_1)
        expected = [10.1, 2.3, 2.25, 2.2, 2.1]
        self.assertEqual(result, expected)

    # Part 5
    #### Largest_Between Tests
    def test_largest_between_1(self):
        result = lab5.largest_between([10,9,5,6,2,5], 1, 4)
        expected = 3
        self.assertEqual(result, expected)

    def test_largest_between_2(self):       #normal range between (1,4) not including 1 & 4
        result = lab5.largest_between([10,9,5,6,2,5], 1, 4)
        expected = 3
        self.assertEqual(result, expected)

    def test_largest_between_3(self):       # upper == lower
        result = lab5.largest_between([10,9,5,6,2,5], 4, 4)
        expected = None
        self.assertEqual(result, expected)

    def test_largest_between_4(self):       #lower out of bounds
        result = lab5.largest_between([10,9,5,6,2,5], -2, 4)
        expected = 1
        self.assertEqual(result, expected)

    def test_largest_between_5(self):       #upper out of bounds
        result = lab5.largest_between([10,9,5,6,2,5], 3, 10)
        expected = 4
        self.assertEqual(result, expected)

    def test_largest_between_6(self):       #empty list
        result = lab5.largest_between([], 1, 4)
        expected = None
        self.assertEqual(result, expected)

    # Part 6
    #### Furthest_From_Origin Tests
    def test_furthest_from_origin_1(self):
        p1 = Point(6,7)
        p2 = Point(1,2)
        p3 = Point(5,7)
        points = [p1,p2,p3]
        result = lab5.furthest_from_origin(points)
        expected = 0
        self.assertEqual(result, expected)

    def test_furthest_from_origin_2(self):
        p1 = Point(10,7)
        p2 = Point(9,8)
        p3 = Point(11,6)
        points = [p1,p2,p3]
        result = lab5.furthest_from_origin(points)
        expected = 2
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
