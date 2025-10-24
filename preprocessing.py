import pandas as pd

file_path = r'Dataset/PulseBat Dataset.xlsx'

# Load the dataset from the specified pulsebat datasheet
dataset = pd.read_excel(file_path, sheet_name='Data')

# Drop unnecessary columns
dataset.drop(columns=['Mat', 'No.', 'ID'], inplace=True)

# Remove missing values
dataset.dropna(inplace=True)

# Ensure all numeric columns are numeric
dataset = dataset.apply(pd.to_numeric, errors='ignore')

# Sort by 'Q' (charge quantity)
sortedByQ = dataset.sort_values(by='Q')

# Sort by 'SOC' (state of charge)
sortedBySOC = dataset.sort_values(by='SOC')

#Saving the sorted datasets for later reference
sortedByQ.to_csv('Dataset/sorted_by_Q.csv', index=False)
sortedBySOC.to_csv('Dataset/sorted_by_SOC.csv', index=False)


u_cols = [f'U{i}' for i in range(1, 22)] #creating a list of each cell voltage column (1 - 21)
dataset['AvgCellVoltage'] = dataset[u_cols].mean(axis=1) #calculating average cell voltage for each row
