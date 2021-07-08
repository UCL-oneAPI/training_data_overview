import csv
import sys


def find_warnings(file_path):
    code_str = get_file_str(file_path)
    warnings = extract_warnings(code_str)
    add_to_csv(warnings, file_path)


def get_file_str(file_path: str) -> str:
    return "this is fake data: DPCT1003:xx and DPCT1009:frr plus DPCT1010"


def extract_warnings(code_str: str) -> list:
    return ["DPCT1003", "DPCT1009", "DPCT1010"]


def add_to_csv(warnings: list, file_path: str):
    project_name = file_path.split('/')[0]
    with open('warnings_data.csv', 'a') as f:
        for warning in warnings:
            # fields = {"warning_code": warning,
            #           "project_name": project_name,
            #           "file_path": file_path}
            fields = [warning, project_name, file_path]
            writer = csv.writer(f)
            writer.writerow(fields)


if __name__ == "__main__":
    # create_csv(sys.argv[1:])
    find_warnings(sys.argv[1])
    # find_warnings('other_project/main.cpp')
