import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("air_quality_cleaned.csv")
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("中国城市空气质量可视化"),

    html.Div([
        html.Label("选择城市:"),
        dcc.Dropdown(
            options=[{'label': city, 'value': city} for city in df['city'].unique()],
            id='city_selector',
            value=df['city'].iloc[0]
        ),
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("AQI筛选范围:"),
        dcc.RangeSlider(
            min=int(df['AQI'].min()), max=int(df['AQI'].max()), step=1,
            marks={i: str(i) for i in range(int(df['AQI'].min()), int(df['AQI'].max()) + 1, 20)},
            value=[int(df['AQI'].min()), int(df['AQI'].max())],
            id='aqi_slider'
        ),
    ], style={'width': '98%', 'padding': '20px 0'}),

    dcc.Graph(id='aqi_scatter')
])


@app.callback(
    Output('aqi_scatter', 'figure'),
    Input('city_selector', 'value'),
    Input('aqi_slider', 'value')
)
def update_chart(selected_city, aqi_range):
    filtered = df[(df['city'] == selected_city) &
                  (df['AQI'] >= aqi_range[0]) &
                  (df['AQI'] <= aqi_range[1])]

    fig = px.scatter(
        filtered,
        x='PM2.5', y='AQI',
        color='PM10', size='NO2',
        hover_name='city',
        title=f"{selected_city} AQI 与 PM2.5/PM10/NO2 关系图",
        labels={'PM2.5': 'PM2.5 (μg/m³)', 'AQI': '空气质量指数'}
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
