import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hourly_data = pd.read_csv('../hourly_weather_2_dat.txt',delim_whitespace=True,na_values=['*','**','***','****','*****','******'])
#print (hourly_data)
#uasf code numbers for dfw area weather stations
dfw=722580
lovefield=722580
fort_worth=747390
#hourly_data = pd.read_csv('../hourly_weather_2_dat.txt',delim_whitespace=True)
#index=hourly_data.index[hourly_data['USAF']]
index=hourly_data.loc[0:hourly_data.size-1,'USAF']==dfw
#print(hourly_data[index])

dallas_data=hourly_data.loc[index]
dallas_data=dallas_data.replace('0.00T',0.00,regex=True)
#dallas_data.loc[:,'YR--MODAHRMN']=str(hourly_data['YR--MODAHRMN'])
#print (dallas_data['YR--MODAHRMN'])
dallas_data.loc[:,'YR--MODAHRMN']=pd.to_datetime(dallas_data.loc[:,'YR--MODAHRMN'],format='%Y%m%d%H%M')
# (dallas_data['YR--MODAHRMN'])
time=pd.to_datetime(201710011353,format='%Y%m%d%H%M')
#print(time)


#clean up trace issues in pcp01
#for row in dallas_data.itertuples():
	#print(row)
#	if row.PCP01=='0.00T':
#		print(row)
		#print( row.Index )
#		dallas_data.loc[row.Index,'PCP01']=0.00
#		dallas_data.loc[row.Index,'PCP06']=np.nan

		#print (row)

ax=dallas_data.plot('YR--MODAHRMN','TEMP')
ax=dallas_data.plot('YR--MODAHRMN','DEWP')
ax=dallas_data.plot('YR--MODAHRMN','SPD')
#print (dallas_data['PCP01'])

dallas_data.loc[:,'PCPXX']=pd.to_numeric(dallas_data['PCPXX'],errors='coerce')
dallas_data.loc[:,'PCP24']=pd.to_numeric(dallas_data['PCP24'],errors='coerce')
dallas_data.loc[:,'PCP06']=pd.to_numeric(dallas_data['PCP06'],errors='coerce')
dallas_data.loc[:,'PCP01']=pd.to_numeric(dallas_data['PCP01'],errors='coerce')
ax=dallas_data.plot('YR--MODAHRMN','PCP06',kind='hist')
ax=dallas_data.plot('YR--MODAHRMN','PCP01',kind='hist')
ax=dallas_data.plot('YR--MODAHRMN','PCP24',kind='hist')
ax=dallas_data.plot('YR--MODAHRMN','PCPXX',kind='hist')

print(dallas_data.loc[:,'PCP01'].max())

plt.show()