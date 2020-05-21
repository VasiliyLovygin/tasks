import string

from enum import Enum


def get_number_by_chars(s, sep=string.whitespace):
    word = []

    for char in s:
        if char in sep:
            if word:
                yield int("".join(word))
                word = []
        else:
            word.append(char)
    if word:
        yield int("".join(word))


class SearchStatus(Enum):
    FOUND = 1
    NOT_FOUND = 2


class TwoNumbersSumEqualTarget:

    def __init__(self, input_file_path: str, output_file_path: str):
        self.__input_file = input_file_path
        self.__output_file = output_file_path

        self.__find_status = SearchStatus.NOT_FOUND

    def write_result(self):
        with open("output.txt", "w") as file:
            file.write('1' if self.__find_status == SearchStatus.FOUND else '0')

    def run(self):
        with open(self.__input_file) as f:
            target = f.readline()
            target = int(target)

            tmp_set = set()
            for n in get_number_by_chars(f.readline()):
                if n >= target:
                    continue
                tmp = target - n
                if tmp in tmp_set:
                    self.__find_status = SearchStatus.FOUND
                    break
                else:
                    tmp_set.add(n)

        self.write_result()


task = TwoNumbersSumEqualTarget(input_file_path="input.txt", output_file_path="output.txt")
task.run()
