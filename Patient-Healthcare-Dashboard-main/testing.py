import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from pathlib import Path

try:
    df = pd.read_csv("healthcare_dashbaord/assets/healthcare.cvs")
    df.show(10)
except FileNotFoundError:
    print("file not found") # fallback
