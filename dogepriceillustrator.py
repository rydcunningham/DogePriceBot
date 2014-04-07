import plotly
from datetime import datetime
from dogepricebase import DogePriceBase

database = DogePriceBase()
#Instantiate plotly object, pass username and API key
py = plotly.plotly("dataraptor", "97xc9d5r1u")
graph_data = []
x = []
btcdoge = []
usddoge = []
trace1_text = []
trace2_text = []

tweets = database.c.execute("SELECT * FROM dogePrices ORDER BY month, day, hour").fetchall()
for tweet in tweets:
	timestamp = datetime(tweet[0], tweet[1], tweet[2], tweet[3], tweet[4], second=0)
	x.append(timestamp)
	btcdoge.append(tweet[5])
	usddoge.append(tweet[6])
	trace1_text.append("BTC:DOGE")
	trace2_text.append("USD:DOGE")
	print timestamp, tweet[5]*1000, tweet[6], tweet[7]

trace1 = {
	'name': "BTC:DOGE",
	'x': x,
	'y': btcdoge,
	'text': trace1_text,
	'line':{
		'color':'c4a451',
		'width':5
	},
	'marker':{
		'opacity': 1.0,
		'symbol':'square',
		'size':12,
		'color':'424A87',
		'line':{
			'width':3,
			'color':'424A87'
		},
	},
}

trace2 = {
	'name': "USD:DOGE",
	'x': x,
	'y': usddoge,
	'yaxis':'y2',
	'text': trace2_text,
	'line':{
		'color':'419D41',
		'width':5
	},
	'marker':{
		'opacity': 1.0,
		'symbol':'square',
		'size':12,
		'color':'C45151',
		'line':{
			'width':3,
			'color':'C45151'
		},
	},
}

graph_data.append(trace1)
graph_data.append(trace2)

layout = {
	'xaxis': {
		'title': 'very time',
		'titlefont': {
			'family':'Verdana, sans-serif'
			},
		},
	'yaxis': {
		'title': 'BTC:DOGE',
		'titlefont': {
			'family':'Verdana, sans-serif'
			},
		},
	'yaxis2':{
		'title': '$:DOGE',
		'titlefont': {
			'family':'Verdana, sans-serif'
			},
		'overlaying':'y',
		'side':'right',
		},
	'title': 'Market Dogecoin Prices'
}

py.plot(graph_data, layout=layout,
		filename='Dogecoin Historical Prices', fileopt='overwrite',
		world_readable = True, width = 1000, height = 650)