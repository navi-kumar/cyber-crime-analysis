import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from variables import terms, year_vals


def plot_year(df, year):
	# st.dataframe(df.iloc[:,1:], hide_index=True, column_config=terms)
	
	# ---- Ger MIN/MAX Data ----
	max_CR = df.iloc[:-1, :]['CR'].idxmax()
	min_CR = df.iloc[:-1, :]['CR'].idxmin()

	max_PAR = df.iloc[:-1, :]['PAR'].idxmax()
	min_PAR = df.iloc[:-1, :]['PAR'].idxmin()
	max_PAQ = df.iloc[:-1, :]['PAQ'].idxmax()
	max_PCV = df.iloc[:-1, :]['PCV'].idxmax()



	# ---- Get TOP N Column_Data ----
	sorted_by_CR = df.iloc[:-1].sort_values(by='CR', ascending=False)
	CR_10 = sorted_by_CR.head(10)[['State/UT', 'CR', 'CCS']]
	
	sorted_by_PAR = df.iloc[:-1].sort_values(by='PAR', ascending=False)
	PAR_10 = sorted_by_CR.head(10)[['State/UT', 'PAR']]
	

	# Create a Plotly pie chart
	PAR_other = df.iloc[-1]['PAR'] - PAR_10['PAR'].sum()
	print(PAR_other, PAR_10['PAR'].sum(), df.iloc[-1]['PAR'])

	PAR_last = pd.DataFrame({'State/UT': ['Sum of All remaining States/UTs'], 'PAR': [PAR_other]})
	PAR_10 = pd.concat([PAR_10, PAR_last])

	fig_pie = go.Figure(data=[go.Pie(labels=PAR_10['State/UT'], values=PAR_10['PAR'])])

	# Set chart title
	fig_pie.update_layout(title= f'Persons Arrested in {year} for Cybercrime')

	# Create traces for Value 1 and 
	trace1 = go.Bar(x=CR_10['State/UT'], y=CR_10['CR'], name='Cases Registered', marker=dict(color='green'))
	trace2 = go.Bar(x=CR_10['State/UT'], y=CR_10['CCS'], name='Cases Chargesheeted', marker=dict(color='blue'))

	# Create a layout for the chart
	layout = go.Layout(
	    title=f'Cases Registered in {year} for Cybercrime',
	    xaxis=dict(title='Categories'),
	    yaxis=dict(title='Values')
	)

	# Create a figure with the traces and layout
	fig_bar = go.Figure(data=[trace1, trace2], layout=layout)

	# Adjust the bar width to make them conjoined
	fig_bar.update_traces(width=0.4)



	with st.container():
		st.header(f"Statistics from {year}:")

		col1, col2, col3 = st.columns(3)
		with col1:
			st.write(f"Most Cases Registered:  {df.loc[max_CR, 'State/UT']}")
			st.write(f"Least Cases Registered: {df.loc[min_CR, 'State/UT']}")
		with col2:
			st.write(f"Most People Arrested:  {df.loc[max_PAR, 'State/UT']}")
			st.write(f"Least People Arrested: {df.loc[min_PAR, 'State/UT']}")
		with col3:
			st.write(f"Most People Convicted: {df.loc[max_PCV, 'State/UT']}")
			st.write(f"Most People Acquitted: {df.loc[max_PAQ, 'State/UT']}")


	with st.container():
		st.plotly_chart(fig_bar)
		st.write("#")
		st.write("---")
		st.write("#")
		st.plotly_chart(fig_pie)