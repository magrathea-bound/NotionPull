import requests
import json
import pandas as pd
from notionData import auth, server

#Query Notion page
headers = {
    'Authorization': auth,
    'Notion-Version': '2022-06-28'
}
r = requests.post(f'https://api.notion.com/v1/databases/{server}/query', headers = headers)

exercisePage = r.json()


#Extract information from JSON
load = []
reps = []
dat = []
musc = []
sets = []
exer = []
notes = []

for column in exercisePage['results']:
    prop = column['properties']
    #print(column['properties'])

    exer.append(prop['Exercise']['select']['name'])
    load.append(prop['Load/Speed (Min/Mile)']["number"])
    reps.append(prop['Reps/Time (Minutes)']["number"])
    dat.append(prop['Date']['date']['start'])
    musc.append(prop['Muscle Group']['select']['name'])
    sets.append(prop['Sets/Distance (Miles)']['number'])
    notes.append(prop['Notes']['title'][0]['plain_text'])


#Create Dataframe
data = {"Exercise":exer, "Load/Pace (Min/Mile)": load, "Reps/Time (Minutes)": reps, "Date": dat, "Muscle Group" : musc, "Sets/Distance (Miles)": sets, "Name":notes}
df = pd.DataFrame(data)

df.to_csv('ExerciseLog.csv', index=False)
