import streamlit as st
import pandas as pd
import numpy as np
import requests
from streamlit_lottie import st_lottie
from state import plot_state
from years import plot_year
from variables import terms, year_vals

# import plotly.express as px

st.set_page_config(page_title='Crime Analysis', page_icon=":bar_chart:", layout="wide")

st.markdown("""
        <style>
               .block-container {
                    padding-top: 5rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)


# ---------------- Load Files -----------------
overall = pd.read_csv('data/data_overall.csv')
stations = pd.read_csv('data/data_stations.csv')
y_2017 = pd.read_csv('data/data_17.csv')
y_2018 = pd.read_csv('data/data_18.csv')
y_2019 = pd.read_csv('data/data_19.csv')
y_2020 = pd.read_csv('data/data_20.csv')
y_2021 = pd.read_csv('data/data_21.csv')


stations.iloc[:-1] = stations.iloc[:-1].sort_values(by='Number of Cyber Crime Police Stations', ascending=False).reset_index(drop=True)
# stations_sum = stations.iloc[-1]
# stations = stations.iloc[:-1,:].sort_values(by='Number of Cyber Crime Police Stations', ascending=False)
# stations = pd.concat([stations, stations_sum])

#------ Header Section -------
with st.container():
	st.title("Cybercrime Analysis!!")
	st.write("Here's a [link to the data](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=1883066), released by Govt. of India, was used for this analysis !")


analysis_options = ["Overall", "Year-wise analysis", "State/UT based analysis"]

with st.container():
	analysis_option = st.radio("**Analysis Option:**", analysis_options, horizontal=True)
	st.write("---")
	st.write("#")

	if analysis_option == "Overall":
		st.dataframe(overall[['State/UT', 'CR', 'CON', 'CAQ', 'PAR', 'PCV', 'PAQ']], hide_index=True, column_config=terms, use_container_width=True)
		st.dataframe(stations.iloc[:,2:], hide_index=True)

	elif analysis_option == "Year-wise analysis":

		with st.container():
			st.subheader("Choose Year:")		#--------make these two inline
			year = st.radio("", ["Year 2017", "Year 2018", "Year 2019", "Year 2020", "Year 2021"], horizontal=True, label_visibility='collapsed')	

			if year == "Year 2017"	: plot_year(y_2017, "2017")

			elif year == "Year 2018": plot_year(y_2018, "2018")

			elif year == "Year 2019": plot_year(y_2019, "2019")

			elif year == "Year 2020": plot_year(y_2020, "2019")

			elif year == "Year 2021": plot_year(y_2021, "2021")


	elif analysis_option == "State/UT based analysis":
		st.subheader("Select a State/UT")
		state = st.selectbox("Select a State/UT:", overall.iloc[:-1, 1], label_visibility='collapsed')
		df_loc = pd.concat([y_2017[y_2017["State/UT"]==state],
							y_2018[y_2018["State/UT"]==state],
							y_2019[y_2019["State/UT"]==state],
							y_2020[y_2020["State/UT"]==state],
							y_2021[y_2021["State/UT"]==state]], 
							keys=year_vals).reset_index(level=1, drop=True)

		plot_state(state, df_loc)
