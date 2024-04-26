import csv

def remove_duplicates(csv_file, cleaned_csv_file):
    unique_lines = set()
    cleaned_data = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            line = ','.join(row)
            if line not in unique_lines:
                unique_lines.add(line)
                cleaned_data.append(row)

    with open(cleaned_csv_file, 'w', newline='') as cleaned_file:
        writer = csv.writer(cleaned_file)
        writer.writerows(cleaned_data)

# Example usage:
remove_duplicates('cleaned_data1.csv', 'no_repition_data.csv')