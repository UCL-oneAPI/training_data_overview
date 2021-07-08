import csv
import re
import sys

'''
Run this command with e.g. $ python warnings_count.py "sample_files/project1/main.dp.cpp"
Paths to sample files are:
    "sample_files/project1/main.dp.cpp"
    "sample_files/bpnn/bpnn_layerforward.h"
    "sample_files/project1/simpleAtomicIntrinsics_kernel.dp.hpp"
'''


def find_warnings(file_path):
    warnings_at_lines = extract_warnings(file_path)
    add_to_csv(warnings_at_lines, file_path)


def extract_warnings(file_path: str) -> list:
    warnings_at_lines = []
    with open(file_path, "r") as f:
        code_lines_strings = f.readlines()
        pattern = ".*(DPCT\d{4}):\d+: "

        for i in range(len(code_lines_strings)):
            code_line = code_lines_strings[i]
            result = re.search(pattern, code_line)
            if result:
                warning_code = result.group(1)
                warnings_at_lines.append((warning_code, i + 1))

    return warnings_at_lines


def add_to_csv(warnings: list, file_path: str):
    project_name = get_project_name(file_path)
    with open('warnings_data.csv', 'a') as f:
        for warning in warnings:
            warning_code = warning[0]
            line_in_file = warning[1]
            fields = [warning_code, project_name, file_path, line_in_file]
            writer = csv.writer(f)
            writer.writerow(fields)


def get_project_name(file_path: str):
    path_splits = file_path.split('/')
    if path_splits[0] == "sample_files":
        return path_splits[1]
    else:
        return path_splits[0]


if __name__ == "__main__":
    find_warnings(sys.argv[1])
