import csv


def create_csv():
    # to reset sample data, use path 'warnings_data.csv' instead
    with open('../../../training_data_overview/warnings_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['warning_code', 'project_name', 'file_path', 'line_in_file']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


if __name__ == "__main__":
    create_csv()
    print('created new csv to fill')
