import pandas as pd

# creating the DataFrame
cars_data = pd.DataFrame({'Cars': ['BMW', 'Audi', 'Bugatti',
                                   'Porsche', 'Volkswagen'],
                          'MaxSpeed': [220, 230, 240, 210, 190],
                          'Color': ['Black', 'Red', 'Blue',
                                    'Violet', 'White']})

# writing to Excel
datatoexcel = pd.ExcelWriter('CarsData1.xlsx')

# write DataFrame to excel
cars_data.to_excel(datatoexcel)

# save the excel
datatoexcel.close()
print('DataFrame is written to Excel File successfully.')