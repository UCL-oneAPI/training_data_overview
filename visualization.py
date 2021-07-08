import csv


def visualize_results():
    warning_rows = get_rows()
    for row in warning_rows:
        # Todo: replace print with visualization
        print(f'warning type: {row[0]}. project name: {row[1]}. path to file: {row[2]}.')


def get_rows():
    with open('warnings_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        warnings = []

        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # skip header
                pass
            else:
                warnings.append([row[0], row[1], row[2]])
            line_count += 1

        return warnings


if __name__ == "__main__":
    visualize_results()
