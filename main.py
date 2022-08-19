import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

# ------------------------------------------------------------------------

# Data from https://covidtracking.com/api/
# Filter Data

df = pd.read_csv("covid-19-states-daily.csv")
df['dateChecked'] = pd.to_datetime(df['dateChecked'])
df = df[df['dateChecked'].dt.date.astype(str) == '2020-03-17']
df = df[df['death'] >= 5]
print(df)

pie_chart = px.pie(
    data_frame=df,
    values='death',
    names='state',
    color='state',  # Differentiate markers (discrete) by color
    color_discrete_sequence=["red", "green", "blue", "orange"],  # Set marker colors
    # color_discrete_map={"WA":"yellow","CA":"red","NY":"black","FL":"brown"},
    hover_name='negative',  # Values appear in bold in the hover tooltip
    # hover_data=['positive'],            # Values appear as extra data in the hover tooltip
    # custom_data=['total'],              # Values are extra data to be used in Dash callbacks
    labels={"state": "the State"},  # Map the labels
    title='Coronavirus in the USA',  # Figure title
    template='presentation',  # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
    # 'plotly_white', 'plotly_dark', 'presentation',
    # 'xgridoff', 'ygridoff', 'gridon', 'none'
    width=800,  # Figure width in pixels
    height=600,  # Figure height in pixels
    hole=0.5,  # Represents the hole in middle of pie
)

pie_chart.update_traces(textposition='outside', textinfo='percent+label',
                        marker=dict(line=dict(color='#000000', width=4)),
                        pull=[0, 0, 0.2, 0], opacity=0.7, rotation=180)

pio.show(pie_chart)
