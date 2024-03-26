import pandas as pd
import glob

# Specify the path to your folder and the pattern to match CSV files
folder_path = 'review_tab_splits\*.csv'

# Retrieve a list of CSV file paths in the folder
csv_files = glob.glob(folder_path)



# List of CSV file paths
# csv_files = ['path/to/your/file1.csv', 'path/to/your/file2.csv', 'path/to/your/file3.csv']

# Read the first CSV file
combined_df = pd.read_csv(csv_files[0])

# Loop through the remaining CSV files and append them to the combined DataFrame
for file in csv_files[1:]:
    temp_df = pd.read_csv(file)
    combined_df = pd.concat([combined_df, temp_df], ignore_index=True)

# Check for duplicate rows across the combined DataFrame
# You can specify subset=['column1', 'column2', ...] to check duplicates based on specific columns
duplicate_rows = combined_df[combined_df.duplicated()]

# Remove duplicate rows across the combined DataFrame
# You can specify subset=['column1', 'column2', ...] to check duplicates based on specific columns
# keep='first' keeps the first occurrence of each duplicate row, you can use keep='last' or keep=False to discard all duplicates
cleaned_df = combined_df.drop_duplicates(keep='first')


# after remove duplicate
# dup = cleaned_df[cleaned_df.duplicated()]


# null_count = cleaned_df.isnull().sum()
# print(null_count)


# chunk_size = 600  # Adjust the number of rows per file as needed
# num_chunks = len(cleaned_df) // chunk_size + (1 if len(cleaned_df) % chunk_size else 0)

# for i in range(num_chunks):
#     new_df = cleaned_df[i*chunk_size:(i+1)*chunk_size]
#     new_df.to_csv(f'Review files/Review_file_{i+1}.csv', index=False)

# Print or process the duplicate rows
# print(cleaned_df)
# print(dup)
