# Import Tabula
import tabula

# Read PDF into a list of DataFrame
dfs = tabula.read_pdf('code_files\practice questions\NEET-2024-Sample-Paper-with-Solutions-PDF.pdf', pages='all', multiple_tables=True)

# Print each DataFrame (each table is a DataFrame)
for df in dfs:
    print(df)
