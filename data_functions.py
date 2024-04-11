import csv
def get_csv_data():
    file_path = "sample_data.csv"
    csv_data = []
    with open(file_path, encoding='utf-8') as file:
        csvReader = csv.DictReader(file)
        csv_data = [row for row in csvReader]
    return csv_data

# print(get_csv_data()[0]['Code'])