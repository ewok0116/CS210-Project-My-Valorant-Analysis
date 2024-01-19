
import pandas as pd

# Assuming csv_file1 and csv_file2 are your CSV files
csv_file1 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON1.csv"
csv_file2 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON2.csv"
csv_file3 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON3.csv"
csv_file4 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON4.csv"
csv_file5 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON5.csv"
csv_file6 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON6.csv"
csv_file7 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON7.csv"
csv_file8 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON8.csv"
csv_file9 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON9.csv"
csv_file10 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON10.csv"
csv_file11 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON11.csv"
csv_file12 = "/Users/ecemcakalli/Desktop/burcu_deneme/csv files/JSON12.csv"





# Read the CSV files into pandas DataFrames
df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)
df3 = pd.read_csv(csv_file3)
df4 = pd.read_csv(csv_file4)
df5 = pd.read_csv(csv_file5)
df6 = pd.read_csv(csv_file6)
df7 = pd.read_csv(csv_file7)
df8 = pd.read_csv(csv_file8)
df9 = pd.read_csv(csv_file9)
df10 = pd.read_csv(csv_file10)
df11 = pd.read_csv(csv_file11)
df12 = pd.read_csv(csv_file12)




# Concatenate the DataFrames along rows (axis=0)
combined_df = pd.concat([df1, df2, df3, df4, df5,df6,df7,df8,df9,df10,df11, df12], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv("CS210_CombinedCSVs.csv", index=False)
