import csv


def create_warnings_csv():
    with open('warnings_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['warning_code', 'project_name',
                      'file_path', 'line_in_file', 'message_id', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def create_messages_csv():
    with open('warning_messages.csv', 'w', newline='') as csvfile:
        fieldnames = ['message_id', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


if __name__ == "__main__":
    create_warnings_csv()
    create_messages_csv()
    print('created new blank CSVs for warnings and for unique messages.')
