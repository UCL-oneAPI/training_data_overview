import csv
import re
import sys

'''
Run this command with e.g. $ python warnings_count.py "sample_files/project1/main.dp.cpp"
Paths to sample files are:
    "sample_files/project1/main.dp.cpp"
    "sample_files/bpnn/bpnn_layerforward.h"
    "sample_files/project1/simpleAtomicIntrinsics_kernel.dp.hpp"
    
But this can be done for any other file as well.
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
            code_line = code_lines_strings[i].lstrip()
            result = re.search(pattern, code_line)
            if result:
                warning_code = result.group(1)
                for j in range(1, len(code_lines_strings) - i):
                    next_line = code_lines_strings[i + j]
                    end_comment_pattern = "\*\/"
                    is_comment_end = re.search(end_comment_pattern, next_line)
                    if is_comment_end:
                        lines_without_indentation = [line.lstrip() for line in code_lines_strings[i:i + j]]
                        msg = ''.join(lines_without_indentation)
                        msg_excl_warning_code = msg[result.regs[0][1]:]
                        break
                warnings_at_lines.append((warning_code, i + 1, msg_excl_warning_code))

    return warnings_at_lines


def add_to_csv(warnings: list, file_path: str):
    project_name = get_project_name(file_path)
    is_sample_path = is_sample_file_path(file_path)
    csv_path = 'warnings_data.csv' if is_sample_path \
        else '../../../training_data_overview/warnings_data.csv'
    with open(csv_path, 'a') as f:
        for warning in warnings:
            warning_code = warning[0]
            line_in_file = warning[1]
            full_message = warning[2]
            message_id = get_message_id(warning[2], is_sample_path)
            fields = [warning_code, project_name,
                      file_path, line_in_file,
                      message_id, full_message]
            writer = csv.writer(f)
            writer.writerow(fields)


def get_message_id(message, is_sample_path):
    csv_path = 'warning_messages.csv' if is_sample_path \
        else '../../../training_data_overview/warning_messages.csv'
    highest_id = 0
    with open(csv_path, 'r') as f:
        is_header = True
        for row in csv.reader(f):
            if is_header:
                is_header = False
                continue
            current_id = int(row[0]) if row[0] is not None else 0
            if row[1] == message:
                # return id if found
                return current_id
            if current_id > highest_id:
                highest_id = current_id

    # add message to csv if not found
    with open(csv_path, 'a') as f:
        message_id = highest_id + 1
        fields = [message_id, message]
        writer = csv.writer(f)
        writer.writerow(fields)
        return message_id


def get_project_name(file_path: str):
    path_splits = file_path.split('/')
    if is_sample_file_path(file_path):
        return path_splits[1]
    else:
        for i in range(len(path_splits)):
            if path_splits[i] == "oneAPI-DirectProgramming-training":
                return path_splits[i + 1]
        raise Exception('Folder "oneAPI-DirectProgramming-training" not found.')


def is_sample_file_path(file_path: str):
    path_splits = file_path.split('/')
    if path_splits[0] == "sample_files":
        return True
    return False


if __name__ == "__main__":
    find_warnings(sys.argv[1])
