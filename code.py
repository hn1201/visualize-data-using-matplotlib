# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

electors_2009 = pd.read_csv(path)
candidate_2009 = pd.read_csv(path1)

# Plot a bar chart to compare the number of male and female candidates in the election
candidate_2009['Candidate_Sex'].value_counts().plot(kind="bar", figsize=(6,6))
plt.xticks(rotation=45)
plt.ylabel("No. of Voters")
# Plot a histogram of the age of all the candidates as well as of the winner amongst them. Compare them and note an observation
candidate_2009.hist(['Candidate_Age'], bins=10)
candidate_2009[candidate_2009['Position'] == 1].hist(['Candidate_Age'], bins=10)
# Plot a bar graph to get the vote shares of different parties
vote_share = candidate_2009.groupby(['Party_Abbreviation'])['Total_Votes_Polled'].sum()
plt_bar_chart = vote_share.sort_values(ascending=False)[:10].plot(kind='bar')
plt_bar_chart.set_xlabel('Vote_Share')
plt_bar_chart.set_ylabel('Party')
plt_bar_chart.set_title('Vote Share of top 10 parties')
# Plot a barplot to compare the mean poll percentage of all the states
electors_2009.groupby(['STATE'])[['POLL PERCENTAGE']].mean().plot(kind="bar", stacked=False, figsize=(10,10))

# Plot a bar plot to compare the seats won by different parties in Uttar Pradesh
Seats_Won = candidate_2009[(candidate_2009['State_name']=='Uttar Pradesh') & (candidate_2009['Position']==1)]['Party_Abbreviation'].value_counts()
plt.bar(Seats_Won.index, Seats_Won)
plt.xlabel('Parties')
plt.ylabel('Seat-Won')
plt.title("Seats won by different parties in UP")
# Plot a stacked bar chart to compare the number of seats won by different `Alliances` in Gujarat,Madhya Pradesh and Maharashtra. 
mask_1 = (candidate_2009['Position'] == 1)
mask_2 = (candidate_2009['State_name'].isin(['Gujrat', 'Madhya Pradesh', 'Maharashtra']))
Seats_Reqd_States = candidate_2009[mask_1 & mask_2][['State_name', 'Alliance']]
res = Seats_Reqd_States.groupby(['State_name', 'Alliance']).size().unstack()
res.plot(kind='bar', stacked=True, figsize=(15,10))
# Plot a grouped bar chart to compare the number of winner candidates on the basis of their caste in the states of Andhra Pradesh, Kerala, Tamil Nadu and Karnataka
mask_1 = (candidate_2009['Position'] == 1)
mask_2 = (candidate_2009['State_name'].isin(['Andhra Pradesh', 'Kerala', 'Tamil Nadu', 'Karnataka']))
Winning_Candidates = candidate_2009[mask_1 & mask_2]
res = Winning_Candidates.groupby(['State_name', 'PC_Type'])['Position'].sum().unstack()
res.plot(kind='bar', figsize=(15,10))
# Plot a horizontal bar graph of the Parliamentary constituency with total voters less than 100000
mask = (electors_2009['Total voters'] < 100000)
val = electors_2009[mask]
plt.barh(val['PARLIAMENTARY CONSTITUENCY'], val['Total voters'])
plt.xlabel("Count")
plt.ylabel("PC")
plt.title("PC vs Electors")
# Plot a pie chart with the top 10 parties with majority seats in the elections
top_10 = candidate_2009[candidate_2009['Position']==1]['Party_Abbreviation'].value_counts()[:10]
top_10.plot.pie(figsize=(10,10), autopct='%.2f')
# Plot a pie diagram for top 9 states with most number of seats
print(electors_2009.groupby(['STATE'])[['PC NO']].count().idxmax())



