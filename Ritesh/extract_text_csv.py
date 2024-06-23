import csv

def extract_and_replace_csv(file_path):
    result_string = ""

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        lines = csvfile.readlines()
        for line in lines:
            # Replace double quotes with #
            modified_line = line.replace('"', '#')
            result_string += modified_line

    return result_string


file_path = 'tables/5fd87c6a0f6adGazette_Notification_Labelling_Display_14_12_2020/5fd87c6a0f6adGazette_Notification_Labelling_Display_14_12_2020(4).csv'


# Extract text and replace double quotes with #
csv_text = extract_and_replace_csv(file_path)

print(csv_text)
