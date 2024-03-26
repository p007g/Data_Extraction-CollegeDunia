import pandas as pd

'''
file_name = "Reviews_all_pages10"

file_path = f"../Review_tab/Review_tab_updated/{file_name}.csv"
df = pd.read_csv(file_path)



df = df.drop('Review2', axis=1)


chunk_size = 600  # Adjust the number of rows per file as needed
num_chunks = len(df) // chunk_size + (1 if len(df) % chunk_size else 0)

for i in range(num_chunks):
    new_df = df[i*chunk_size:(i+1)*chunk_size]
    new_df.to_csv(f'../Review_tab/review_tab_splits/{file_name}_split_{i+1}.csv', index=False)
'''

try:
    # Step 1: Read the CSV File
    file_name = "Institutes20"

    file_path = f"../Institute_programs/{file_name}.csv"
    df = pd.read_csv(file_path)

    # Collect the names of all columns that existed before adding the new split columns
    original_columns = df.columns.tolist()

    # Step 2: Initial Split by Comma
    initial_split = df['Course_Name'].str.split(',', expand=True)

    # Dynamically name the initial split columns
    initial_split.columns = [f'Course_{i+1}' for i in range(initial_split.shape[1])]


    # Concatenate the initial split columns back into the original DataFrame
    df = pd.concat([df, initial_split], axis=1)

    # Step 3: Further Split Each 'Split_' Column by Colon and Keep Track of New Column Names
    new_columns = []  # List to keep track of all new column names
    for column in initial_split.columns:
        split_by_colon = initial_split[column].str.split(':', expand=True)
        num_cols = split_by_colon.shape[1]
        col_names = [f'{column}.{i+1}' for i in range(num_cols)]
        new_columns.extend(col_names)  # Add new column names to the list
        split_by_colon.columns = col_names
        df = pd.concat([df, split_by_colon], axis=1)
        
        
    # Step 4: Specify Position to Insert New Columns
    insert_position = 3  # Insert starting from the 4th position


    # Insert the new column names into the original_columns list at the specified position
    for c in reversed(new_columns):
        original_columns.insert(insert_position, c)

    # Reorder the DataFrame's columns according to the updated original_columns list
    df = df[original_columns]

    # Optional: Drop the original column that was split, if desired
    df = df.drop('Course_Name', axis=1)


    # Step 5: Save the Result to a New CSV File
    df.to_csv(f"../Institute_programs/{file_name}_updated.csv", index=False)
    print(df)
    
except Exception as e:
    print(e)