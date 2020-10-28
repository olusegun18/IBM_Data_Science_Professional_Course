import os
import pandas as pd

excel = pd.ExcelFile('ASSIGNMENT2.xlsx')
dframe1 = excel.parse('Sheet1')
dframe2 = excel.parse('Sheet2')
dframe3 = excel.parse('Sheet3')
dframe4 = excel.parse('Sheet4')
dframe5 = excel.parse('Sheet5')
dframe6 = excel.parse('Sheet6')
dframe7 = excel.parse('Sheet7')
dframe8 = excel.parse('Sheet8')
dframe9 = excel.parse('Sheet9')
dframe10 = excel.parse('Sheet10')
# print(dframe)


dframe1.to_csv('Sheet1.csv', index = False)
dframe2.to_csv('Sheet2.csv', index = False)
dframe3.to_csv('Sheet3.csv', index = False)
dframe4.to_csv('Sheet4.csv', index = False)
dframe5.to_csv('Sheet5.csv', index = False)
dframe6.to_csv('Sheet6.csv', index = False)
dframe7.to_csv('Sheet7.csv', index = False)
dframe8.to_csv('Sheet8.csv', index = False)
dframe9.to_csv('Sheet9.csv', index = False)
dframe10.to_csv('Sheet10.csv', index = False)