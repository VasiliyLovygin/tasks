import itertools as it
import typing

from enum import Enum


class SearchStatus(Enum):
    FOUND = 1
    NOT_FOUND = 2
    ERROR = 3


class TwoNumbersSumEqualTarget:

    def __init__(self, input_file_path: str, output_file_path: str):
        self.__input_file = input_file_path
        self.__output_file = output_file_path

        self.__find_status = SearchStatus.NOT_FOUND

    def read_params(self) -> typing.Optional[str]:
        try:
            with open(self.__input_file) as f:
                return f.read()
        except:
            self.__find_status = SearchStatus.ERROR

    def write_result(self):
        if self.__find_status != SearchStatus.ERROR:
            try:
                with open("output.txt", "w") as file:
                    file.write('1' if self.__find_status == SearchStatus.FOUND else '0')
            except:
                pass

    def run(self):
        if input_params := self.read_params():
            target, numbers_list = input_params.split('\n')
            target = int(target)
            numbers = [int(x) for x in numbers_list.split() if 0 < int(x) <= target]

            for seq in it.combinations(numbers, 2):
                if sum(seq) == target:
                    self.__find_status = SearchStatus.FOUND
                    break

        self.write_result()


task = TwoNumbersSumEqualTarget(input_file_path="input.txt", output_file_path="output.txt")
task.run()
