from turtle import bgcolor
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from plotly.graph_objects import *


app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='College+', className='title-main'),

    html.H2(id='title-output', className='title-output'),

    dcc.Graph(id='college-barchart', className='graph'),
    
    dcc.Dropdown(
      id='dropdown', 
      options=[
        {"label": "Top SAT Average Score", "value": "SAT_AVG_M"},
        {"label": "Bottom SAT Average Score", "value": "SAT_AVG_L"},
        {"label": "Most Expensive In-State Tuition Fees", "value": "TUITIONFEE_IN_M"},
        {"label": "Least Expensive In-State Tuition Fees", "value": "TUITIONFEE_IN_L"},
        {"label": "Most Expensive Out-of-State Tuition Fees", "value": "TUITIONFEE_OUT_M"},
        {"label": "Least Expensive Out-of-State Tuition Fees", "value": "TUITIONFEE_OUT_L"}
      ],
      value="SAT_AVG_M",
      className='dropdown',
      clearable=False
    ),
])

@app.callback(Output('college-barchart', 'figure'), [Input('dropdown', 'value')])
def update_figure(selected_value):
  df = pd.read_csv('../../dataset/nccolleges.csv')
  if selected_value == "SAT_AVG_M":
    df = df[df["SAT_AVG"].notnull()].sort_values(by=["SAT_AVG"], ascending=[True]).tail(10).reset_index()
    y_axis = "SAT_AVG"
    labels = {"INSTNM": "College", "SAT_AVG": "Average SAT Score"}

  elif selected_value == "SAT_AVG_L":
    df = df[df["SAT_AVG"].notnull()].sort_values(by=["SAT_AVG"], ascending=[True]).head(10).reset_index()
    y_axis = "SAT_AVG"
    labels = {"INSTNM": "College", "SAT_AVG": "Average SAT Score"}

  elif selected_value == "TUITIONFEE_IN_M":
    df = df[df["TUITIONFEE_IN"].notnull()].sort_values(by=["TUITIONFEE_IN"], ascending=[True]).tail(10).reset_index()
    y_axis = "TUITIONFEE_IN"
    labels = {"INSTNM": "College", "TUITIONFEE_IN": "In-State Tuition Fees"}

  elif selected_value == "TUITIONFEE_IN_L":
    df = df[df["TUITIONFEE_IN"].notnull()].sort_values(by=["TUITIONFEE_IN"], ascending=[True]).head(10).reset_index()
    y_axis = "TUITIONFEE_IN"
    labels = {"INSTNM": "College", "TUITIONFEE_IN": "In-State Tuition Fees"}

  elif selected_value == "TUITIONFEE_OUT_M":
    df = df[df["TUITIONFEE_OUT"].notnull()].sort_values(by=["TUITIONFEE_OUT"], ascending=[True]).tail(10).reset_index()
    y_axis = "TUITIONFEE_OUT"
    labels = {"INSTNM": "College", "TUITIONFEE_OUT": "Out-of-State Tuition Fees"}
  
  elif selected_value == "TUITIONFEE_OUT_L":
    df = df[df["TUITIONFEE_OUT"].notnull()].sort_values(by=["TUITIONFEE_OUT"], ascending=[True]).head(10).reset_index()
    y_axis = "TUITIONFEE_OUT"
    labels = {"INSTNM": "College", "TUITIONFEE_OUT": "Out-of-State Tuition Fees"}
  
  fig = px.bar(
      df, 
      x="INSTNM", 
      y=y_axis, 
      labels=labels,
      color=y_axis,
      color_continuous_scale=px.colors.sequential.algae,
      hover_name="INSTNM",
      height=400,
  )
  return fig

@app.callback(
  Output('title-output', 'children'), Input('dropdown', 'value')
)
def update_title(selected_value):
  if selected_value == "SAT_AVG_M":
    return 'Top NC Colleges by SAT Average'
  elif selected_value == "SAT_AVG_L":
    return 'Bottom NC Colleges by SAT Average'
  elif selected_value == "TUITIONFEE_IN_M":
    return 'Most Expensive NC Colleges by In-State Tuition Fee'
  elif selected_value == "TUITIONFEE_IN_L":
    return 'Least Expensive NC Colleges by In-State Tuition Fee'
  elif selected_value == "TUITIONFEE_OUT_M":
    return 'Most Expensive NC Colleges by Out-of-State Tuition Fee'
  elif selected_value == "TUITIONFEE_OUT_L":
    return 'Least Expensive NC Colleges by Out-of-State Tuition Fee'

if __name__ == '__main__':
    app.run_server(debug=True)
