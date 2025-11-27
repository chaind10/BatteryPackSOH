import pandas as pd

file_path = r'PulseBat Dataset.xlsx'

# Load the dataset from the specified pulsebat datasheet
dataset = pd.read_excel(file_path, sheet_name='SOC ALL')

# Drop unnecessary columns
dataset.drop(columns=['Mat', 'No.', 'ID', 'Qn', 'Pt'], inplace=True)

# Remove missing values
dataset.dropna(inplace=True)

# Sort by 'Q' (charge quantity)
#sortedByQ = dataset.sort_values(by='Q')

# Sort by 'SOC' (state of charge)
#sortedBySOC = dataset.sort_values(by='SOC')

#Saving the sorted datasets for later reference
#sortedByQ.to_csv('Dataset/sorted_by_Q.csv', index=False)
#sortedBySOC.to_csv('Dataset/sorted_by_SOC.csv', index=False)