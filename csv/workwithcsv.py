import csv


def read(file_path: str):
    with open(file_path) as file:
        return list(csv.reader(file, delimiter=' ', quotechar='|'))


def write(file_path: str, list_of_rows: str):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in list_of_rows:
            writer.writerow(row)
