from enum import Enum

import typing


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

            tmp_set = set()
            for number in numbers:
                print(number)
                tmp = target - number
                if tmp in tmp_set:
                    self.__find_status = SearchStatus.FOUND
                    break
                else:
                    tmp_set.add(number)

        self.write_result()


task = TwoNumbersSumEqualTarget(input_file_path="input.txt", output_file_path="output.txt")
task.run()
