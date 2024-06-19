import csv

def merge_multiline_rows(file_path):
    merged_rows = []
    current_row = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        
        for row in csvreader:
            if not any(row):  # Skip completely empty rows
                continue

            if not current_row:  # Start a new row if current_row is empty
                current_row = row
            else:
                if row[0] == '':  # Handle multiline data continuation
                    for i in range(len(row)):
                        if row[i]:
                            current_row[i] = current_row[i].strip() + ' ' + row[i].strip()
                else:  # If it's a new row, append the current row to merged_rows and start a new one
                    merged_rows.append(current_row)
                    current_row = row

        if current_row:
            merged_rows.append(current_row)  # Append the last row

    return merged_rows

def convert_rows_to_string(rows):
    result_string = ""
    for row in rows:
        result_string += ",".join(row) + "\n"
    return result_string


# Specify the path to your CSV file
file_path = 'tables/5fd87c6a0f6adGazette_Notification_Labelling_Display_14_12_2020/5fd87c6a0f6adGazette_Notification_Labelling_Display_14_12_2020(6).csv'


# Merge multiline rows and convert to string
merged_rows = merge_multiline_rows(file_path)
result_string = convert_rows_to_string(merged_rows)

print(result_string)
