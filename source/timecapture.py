from input import inputhandler
from merge import intervalmerger
import time
from prettytable import PrettyTable

#
class MergeTimeCapture:
    input_count = [5, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 20000000]
    input = inputhandler.InputHandler()
    merger = intervalmerger.IntervalMerger()

    def run(self):
        table = PrettyTable()
        table.field_names = ["interval_count", "duration (ms)"]
        for count in self.input_count:
            input_data = self.input.generate_test_data(count)
            start_time = time.time()
            self.merger.merge(input_data)
            end_time = time.time()
            print(str(count) + " done!")
            duration = (end_time - start_time) * 1000
            table.add_row([str(count), str(round(duration, 5))])

        print(table)


if __name__ == '__main__':
    MergeTimeCapture().run()
