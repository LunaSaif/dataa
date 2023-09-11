import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Load the data
data url = "https://github.com/LunaSaif/dataa/blob/main/hotstar.csv"
data = pd.read_csv(data_url)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Disney Hotstar TV and Movie Catalog"),
    
    # Create a bar chart for genre vs. year
    dcc.Graph(id='genre-year-bar', figure=px.bar(data, x='genre', y='year')),
    
    # Create another bar chart for genre vs. year (just for demonstration)
    dcc.Graph(id='genre-year-bar-2', figure=px.bar(data, x='genre', y='year')),
    
    # Create a pie chart for type counts
    dcc.Graph(id='type-pie', figure=data['type'].value_counts().plot(kind="pie")),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
