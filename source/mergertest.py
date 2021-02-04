import unittest
from merge import intervalmerger

# unittests for interval merger
class TestMerger(unittest.TestCase):
    test_merger = intervalmerger.IntervalMerger

    def setUp(self):
        self.test_merger = intervalmerger.IntervalMerger()

    # test with valid data that has no intersecting intervals
    def test_valid_data_non_intersecting(self):
        in_data = [[1, 2], [3, 4], [5, 6]]
        assert_data = [[1, 2], [3, 4], [5, 6]]

        out_data = self.test_merger.merge(in_data)
        self.assertEqual(assert_data, out_data)

    # test with valid data that can be merged
    def test_valid_data_intersecting(self):
        in_data = [[1, 2], [2, 4], [2, 6], [2, 3]]
        assert_data = [[1, 6]]

        out_data = self.test_merger.merge(in_data)
        self.assertEqual(assert_data, out_data)

    # test with the exact data form the task
    def test_valid_data_test_data(self):
        in_data = [[25, 30], [2, 19], [14, 23], [4, 8]]
        assert_data = [[2, 23], [25, 30]]

        out_data = self.test_merger.merge(in_data)
        self.assertEqual(assert_data, out_data)

    # test with empty input data
    def test_empty_data(self):
        in_data = []
        assert_data = None

        out_data = self.test_merger.merge(in_data)
        self.assertEqual(assert_data, out_data)

    # test when input data is not a list
    def test_invalid_data_no_list(self):
        in_data = ""
        assert_data = None

        out_data = self.test_merger.merge(in_data)
        self.assertEqual(assert_data, out_data)

    # test with input data thats a list, but not has the correct shape
    def test_invalid_data_wrong_array_shape(self):
        in_data = [[25, 30, 31], [2, 19], [1]]
        assert_data = None

        out_data = self.test_merger.merge(in_data)
        self.assertEqual(assert_data, out_data)

    def test_invalid_data_wrong_array_shape(self):
        in_data = [["a", 30], [2, "b"], [1, 5]]
        assert_data = None

        out_data = self.test_merger.merge(in_data)
        self.assertEqual(assert_data, out_data)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMerger)
    runner = unittest.TextTestRunner()
    runner.run(suite)