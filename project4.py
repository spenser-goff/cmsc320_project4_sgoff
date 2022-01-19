# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:10:24 2021

@author: spens
"""

import folium
import requests
import pandas as pd
import warnings
import datetime, time
from datetime import datetime
from datetime import timedelta
warnings.simplefilter(action='ignore', category=FutureWarning)
'''
Part 1: Getting the Data
'''

arrest_table = pd.read_csv("https://cmsc320.github.io/files/BPD_Arrests.csv")

arrest_table = arrest_table[pd.notnull(arrest_table["Location 1"])]

arrest_table["lat"], arrest_table["long"] = arrest_table["Location 1"].str.split(",").str
arrest_table["lat"] = arrest_table["lat"].str.replace("(", "").astype(float)
arrest_table["long"] = arrest_table["long"].str.replace(")", "").astype(float)

arrest_table.head()

'''
Part 2: Making a map
'''
map_osm = folium.Map(location=[39.29, -76.61], zoom_start=11)
map_osm

'''
Part 3: Combining Parts 1 and 2
'''

#races = arrest_table['race'].unique().tolist()
#race_count = arrest_table['race'].value_counts()


#temp1 = arrest_table.loc[arrest_table['incidentOffense'] == "87-Narcotics"]
#temp2 = arrest_table.loc[arrest_table['incidentOffense'] == '87O-Narcotics (Outside)']
#lst = [temp1, temp2]
#narco_arrests = pd.concat(lst)
#print(narco_arrests.lat.median())
#print(narco_arrests.long.median())
#folium.CircleMarker(location=[39.3050529119, -76.6324434714], radius = 5, fill=True, fill_opacity=0.8).add_to(map_osm)


incident_counts = arrest_table.incidentOffense.value_counts()
#high_vol_io = [x for x in incident_counts.tolist() if x >= 100]
incidents = arrest_table.incidentOffense.unique().tolist()

#temp = arrest_table['district'].unique().tolist()
#offense = "87O-Narcotics (Outside)"

#western_incident_counts = western_arrests_table.incidentOffense.value_counts()
#western_charge_counts = western_arrests_table.charge.value_counts()
#western_low_vol_offenses = western_incident_counts[(western_incident_counts < 15) & (western_incident_counts >= 10)]
#western_offense_name = list(western_low_vol_offenses.index)
#criterion = western_arrests_table['incidentOffense'].map(lambda x: x in western_offense_name)
#western_arrests_table = western_arrests_table[criterion]


#print(W_arrest_table.isnull().sum())
#print(W_arrest_table.isnull().any())
#print(W_arrest_table.isnull().sum() / W_arrest_table.shape[0])
#print(W_arrest_table.info())
#print(W_arrest_table['incidentOffense'].unique())


