# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)
data = data.rename(columns={'Total':'Total_Medals'})
data.head()
#Code starts here



# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event'])

d = data['Better_Event'].value_counts().to_dict()
print(d)

def freqmax(a):
 i = 0
 j = 0
 for each in a.keys():
  if a[each] > i:
   i = a[each]
   j = each
 return j

better_event = freqmax(d)
print(better_event)


# --------------
#Code starts here

top_countries = pd.DataFrame(data = data, columns=['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'])

top_countries = top_countries[:-1]


def top_ten(col):
 
 country_list = []
 country_list= list((top_countries.nlargest(10,col)['Country_Name']))

 return country_list

top_10_summer = top_ten('Total_Summer')
print(top_10_summer)
top_10_winter = top_ten('Total_Winter')
top_10 = top_ten('Total_Medals')

common = [x for x in top_10_summer if x in top_10_winter and top_10]






# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig , (ax_1,ax_2,ax_3) = plt.subplots(3,1)

ax_1.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
ax_2.bar(winter_df['Country_Name'],winter_df['Total_Summer'])
ax_3.bar(top_df['Country_Name'],top_df['Total_Summer'])

ax_1.set_title('Summer')
ax_2.set_title('Winter')
ax_3.set_title('Top 10')




# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']





# --------------
#Code starts here
data_1 =  data[:-1]

data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + data_1['Bronze_Total']

most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']




# --------------
#Code starts here
best=data[data['Country_Name']==best_country] 

print(best.head())
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best.head())
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


