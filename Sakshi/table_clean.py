import csv
import os

# Define the input file path
input_file = 'C:/Users/sakshi/LawMerchant/Sakshi/Book3.csv'

# Define a temporary output file path
temp_file = 'Book2_temp.csv'

try:
    # Read and clean the CSV data
    cleaned_data = []

    with open(input_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row
        num_columns = len(headers)
        current_row = [""] * num_columns

        for row in reader:
            if all(not cell.strip() for cell in row[:-1]):
                current_row[-1] += ' ' + row[-1].strip()
            elif not any(cell.strip() for cell in row[:1]):
                for i in range(1, num_columns):
                    current_row[i] += ' ' + row[i].strip()
            else:
                if current_row != [""] * num_columns:
                    cleaned_data.append(current_row)
                current_row = [cell.strip() for cell in row]

        # Add the last accumulated row
        if current_row != [""] * num_columns:
            cleaned_data.append(current_row)

    # Write the cleaned data to a temporary file
    with open(temp_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write the header
        for row in cleaned_data:
            writer.writerow(row)

    # Replace the original file with the cleaned file
    os.replace(temp_file, input_file)

    print("File cleaned and overwritten successfully.")

except PermissionError:
    print(f"Permission denied: Please close the file '{input_file}' if it is open in another program and try again.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up the temporary file if it exists
    if os.path.exists(temp_file):
        os.remove(temp_file)
