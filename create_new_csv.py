import csv


def create_csv():
    with open('warnings_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['warning_code', 'project_name', 'file_path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


if __name__ == "__main__":
    create_csv()
    print('created new csv to fill')
