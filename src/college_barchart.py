from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# SAT AVERAGE = SAT_AVG
df = pd.read_csv('../dataset/nccolleges.csv')

df = df[df["SAT_AVG"].notnull()]

df = df.sort_values(by=["SAT_AVG"], ascending=[False]).head(10).reset_index()

fig = px.bar(
  df, 
  x="INSTNM", 
  y="SAT_AVG", 
  labels={
  "INSTNM": "College",
  "SAT_AVG": "Average SAT Score"
  },
  color="SAT_AVG",
)

app.layout = html.Div(children=[
    html.H1(children='College+'),

    html.Div(children='''
        Viewing: Top 10 NC Colleges by SAT Scores
    '''),

    dcc.Graph(
        id='college-barchart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
