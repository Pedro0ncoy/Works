from pandas import DataFrame, read_csv
#import matplotlib.pyplot as plt
import pandas as pd

file = r'fuente_inc.xlsx'
df= pd.read_excel(file)
print(df['Incidencia'])

if (df[df['Incidencia'].str.contains('111383356')]):
print("hay una Incidencia")
else:
print("no hay una Incidencia")	

#df = df[df['Incidencia'] != '111383356']


#datos=pd.ExcelFile('fuente_inc.xls')
#print (datos.sheet_names)
#hoja1=datos.parse('Pruebita')
#print(hoja1.index_col)




#print(hoja1.len(col))


#HOJA2 = HOJA1 [HOJA1['Incidencia'] == '111383359'] 

#print ('HOJA2')

#print('Min: ', HOJA1['Incidencia'].min())
#print('Max: ', HOJA1['Incidencia'].max())
#print('Sum: ', HOJA1['Incidencia'].sum())

#print (datos['user.dst'])
#print (datos.ix[0:3])


