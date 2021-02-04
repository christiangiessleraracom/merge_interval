import json
import sys
import random
import re
import os

# get input interval data
class InputHandler:

    file_path = os.path.dirname(__file__) + "/../../input_data.json"
    intRegex = re.compile(r"^([+-]?[1-9]\d*|0)$")


    def fetch_input(self):
        # if no commandline parameter load input data from json file
        if len(sys.argv) <= 1:
            return self.load_from_file()

        # if commandline parameter is integer generate that many random intervals
        if re.match(self.intRegex, sys.argv[1]):
            return self.generate_test_data(int(sys.argv[1]))

        # else assume commandline arg is valid interval data in json array
        try:
            return json.loads(sys.argv[1])
        except:
            print("invalid input data")


    def load_from_file(self):
        with open(self.file_path) as json_file:
            try:
                data = json.load(json_file)
                return data
            except:
                print("invalid input data")

    def generate_test_data(self, count):
        i = 0
        data = []
        max_value = sys.maxsize

        while i < count:
            i += 1
            start = random.randint(0, i * int(max_value / count))
            size = random.randint(1, int(max_value / count))
            data.append([start, start + size])

        return data

    def write_test_data_to_file(self, count):
        data = self.generate_test_data(count)
        with open(self.file_path, 'w') as json_file:
            json_file.write(json.dumps(data))
