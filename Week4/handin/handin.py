import webget
import pandas as pd

url = "https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls/output.xls"
webget.download(url)

# Load spreadsheet
x1 = pd.ExcelFile('output.xls')
# Print the sheet names
print(x1.sheet_names)
#Load a sheet into a DataFrame by name: df1
df= x1.parse('13tbl01')
title = df.iloc[0][0]

print(title)

data= df.iloc[3:4]

data['Unnamed: 2']

for ind, column in enumerate(df.columns):
    print(ind,column)
    if column == 'Unnamed: 2':
        print('hej')