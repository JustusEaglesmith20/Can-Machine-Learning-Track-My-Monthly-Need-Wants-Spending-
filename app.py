from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px
import base64
import io
import pickle

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load your trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app.layout = dbc.Container(
    [
        dbc.NavbarSimple(
            brand="Personal Finance Dashboard",
            brand_href="#",
            color="primary",
            dark=True,
        ),
        html.H1("Personal Finance Dashboard", className="display-3"),
        html.Hr(),
        html.Div([
            html.Img(src=app.get_asset_url('weekly_spending_over_time.gif'))
        ]),
        dcc.Upload(
            id='upload-data',
            children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
            style={
                'width': '100%', 'height': '60px', 'lineHeight': '60px',
                'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                'textAlign': 'center', 'margin': '10px'
            },
            multiple=False
        ),
        html.Div(id='output-data-upload'),
        dcc.Graph(id='bar-chart'),
    ],
    fluid=True,
)

@app.callback(
    Output('bar-chart', 'figure'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    prevent_initial_call=True
)
def update_output(contents, filename):
    if contents:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        else:
            df = pd.read_excel(io.BytesIO(decoded))

        predictions = []
        for _, row in df.iterrows():
            prediction = model.predict([row['Name']])
            predictions.append(prediction[0])

        df['Predicted_Category'] = predictions
        df['Amount'] = df['Amount'].abs()

        # Filter for 'Needs' and 'Wants'
        filtered_df = df[df['Predicted_Category'].isin(['Needs', 'Wants'])]

        # Group by Predicted_Category and sum the Amounts
        category_sums = filtered_df.groupby('Predicted_Category')['Amount'].sum().reset_index()

        # Create the bar chart
        fig = px.bar(category_sums, x='Predicted_Category', y='Amount', 
                     title='Total Spending on Needs and Wants',
                     labels={'Predicted_Category': 'Category', 'Amount': 'Total Amount Spent'},
                     color='Predicted_Category')

        fig.update_layout(
            title_font_size=22,
            yaxis=dict(title='Total Amount'),
            xaxis=dict(title='Category'),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=True,
            margin=dict(l=40, r=40, t=40, b=40)
        )

        return fig

    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)
