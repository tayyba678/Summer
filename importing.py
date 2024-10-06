import pandas as pd

# Specify the paths to your CSV files
file1 = 'ebay_mobile_samsung.csv'
file2 = 'ebay_mobile_appledata.csv'
file3 = 'ebay_mobile_otherbrand.csv'  # Replace with the correct file name

# Read the CSV files into DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

# Combine the DataFrames
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_ebay_mobile_data.csv', index=False, encoding='utf-8')

print("Data merged successfully into 'combined_ebay_mobile_data.csv'")
