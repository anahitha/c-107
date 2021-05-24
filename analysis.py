import pandas as pd
import plotly.graph_objects as go
import csv

data = pd.read_csv('data.csv')
student = input("Enter student id: ")
studentdata = data.loc[data["student_id"]==student]
x = studentdata.groupby(["student_id", "level"], as_index= False)['attempt'].mean()
fig = go.Figure(go.Bar(x = x, y = ['Level 1', 'Level 2', 'level 3', 'level 4'], orientation = 'h'))
fig.show()