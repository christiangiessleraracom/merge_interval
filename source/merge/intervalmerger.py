from input import inputhandler
from output import outputhandler
import numpy as np


# merging intersecting intervals
class IntervalMerger:
    input = inputhandler.InputHandler()
    output = outputhandler.OutputHandler()

    # get input data from handler
    def fetch_input(self):
        return self.input.fetch_input()

    # push merged output data to handler
    def push_output(self, output_data):
        self.output.push_output(output_data)

    def main(self):
        input_data = self.fetch_input()
        output_data = self.merge(input_data)
        self.push_output(output_data)

    # merge the intervals list by using numpy array operation
    def merge(self, input_data):
        try:
            if type(input_data) is not list:
                print("input data is not a list")
                return

            # sort input by starting points and convert to numpy array
            intervals_array = np.asarray(input_data)
            intervals_array.sort(axis=0, kind="mergesort")

            if intervals_array.ndim != 2:
                print("list has wrong shape")
                return

            # getting arrays of starting points and endpoints
            starting_points = intervals_array[:, 0]
            end_points = np.maximum.accumulate(intervals_array[:, 1])

            # create bool array and check for non-intersecting input entries
            intersection_check = np.zeros(len(intervals_array) + 1, dtype=bool)
            intersection_check[0] = True
            intersection_check[-1] = True
            intersection_check[1:-1] = starting_points[1:] > end_points[:-1]

            # build tuples with non-intersecting with arrays of unique start and end entries
            # then then rebuild intervals array by vertically stacking this entries
            interval_point_tuple = (starting_points[:][intersection_check[:-1]], end_points[:][intersection_check[1:]])
            output_data = np.vstack(interval_point_tuple).T

            return output_data.tolist()
        except TypeError:
            print("wrong type in list")
            return
