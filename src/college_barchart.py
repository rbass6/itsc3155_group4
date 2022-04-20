from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

app = Dash(__name__)
# SAT AVERAGE = SAT_AVG

app.layout = html.Div(children=[
    html.H1(children='College+'),

    html.Div(children='''
        Viewing: Top 10 NC Colleges by SAT Scores
    '''),

    dcc.Dropdown(
      id='dropdown', 
      options=[
        {"label": "Average SAT Score", "value": "SAT_AVG"},
        {"label": "In-State Tuition Fees", "value": "TUITIONFEE_IN"},
        {"label": "Out-of-State Tuition Fees", "value": "TUITIONFEE_OUT"},
      ],
      value = "SAT_AVG",
    ),

    dcc.Graph(id='college-barchart')
])

def create_figure():
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
  return fig

@app.callback(Output('college-barchart', 'figure'), [Input('dropdown', 'value')])
def update_figure(selected_value):
  df = pd.read_csv('../dataset/nccolleges.csv')
  if selected_value == "SAT_AVG":
    df = df[df["SAT_AVG"].notnull()].sort_values(by=["SAT_AVG"], ascending=[False]).head(10).reset_index()
    y_axis = "SAT_AVG"
    labels = {"INSTNM": "College", "SAT_AVG": "Average SAT Score"}

  elif selected_value == "TUITIONFEE_IN":
    df = df[df["TUITIONFEE_IN"].notnull()].sort_values(by=["TUITIONFEE_IN"], ascending=[False]).head(10).reset_index()
    y_axis = "TUITIONFEE_IN"
    labels = {"INSTNM": "College", "TUITIONFEE_IN": "In-State Tuition Fees"}

  elif selected_value == "TUITIONFEE_OUT":
    df = df[df["TUITIONFEE_OUT"].notnull()].sort_values(by=["TUITIONFEE_OUT"], ascending=[False]).head(10).reset_index()
    y_axis = "TUITIONFEE_OUT"
    labels = {"INSTNM": "College", "TUITIONFEE_OUT": "Out-of-State Tuition Fees"}
  
  fig = px.bar(
      df, 
      x="INSTNM", 
      y=y_axis, 
      labels=labels,
      color=y_axis,
  )
  return fig
    
if __name__ == '__main__':
    app.run_server(debug=True)
