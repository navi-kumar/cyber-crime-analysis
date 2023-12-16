import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from variables import terms, year_vals


def plot_state(key, df):

	# st.dataframe(df.iloc[:, 2:], column_config = terms)
	
	max_cr = df['CR'].idxmax()
	min_cr = df['CR'].idxmin()

	max_par = df['PAR'].idxmax()
	min_par = df['PAR'].idxmin()



	# ---- Creating Graph Fig ----
	# Create a line chart
	con_line = go.Figure()
	con_line.add_trace(go.Scatter(x=df.index.tolist(), y=df['CON'], mode='lines', name='Cases Convicted'))
	con_line.add_trace(go.Scatter(x=df.index.tolist(), y=df['PCV'], mode='lines', name='Persns Convicted'))

	# Update the layout
	con_line.update_layout(
	    title='Conviction Line Chart',
	    xaxis_title='Year',
	    yaxis_title='No. of Convictions'
	)


	# Create a line chart
	acq_line = go.Figure()
	acq_line.add_trace(go.Scatter(x=df.index.tolist(), y=df['CAQ'], mode='lines', name='Cases Acquitted'))
	acq_line.add_trace(go.Scatter(x=df.index.tolist(), y=df['PAQ'], mode='lines', name='Persons Acquitted'))

	# Update the layout
	acq_line.update_layout(
	    title='Acquittal Line Chart',
	    xaxis_title='Year',
	    yaxis_title='No. of Acquittals'
	)


	with st.container():
		st.header(f"Statistics about {key}:")
		col1, col2 = st.columns(2)

		with col1:
			st.write(f"Most Registered Cases:  {max_cr} ({int(df.loc[max_cr, 'CR'])} Cases)")
			st.write(f"Least Registered Cases: {min_cr} ({int(df.loc[min_cr, 'CR'])} Cases)")
		with col2:
			st.write(f"Most Arrested People:  {max_par} ({int(df.loc[max_par, 'PAR'])} Persons)")
			st.write(f"Least Arrested People: {min_par} ({int(df.loc[min_par, 'PAR'])} Persons)")


	with st.container():
		st.plotly_chart(acq_line)
		st.write("#")
		st.write("---")
		st.write("#")
		st.plotly_chart(con_line)

		# ADD A PIE !?