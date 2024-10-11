import streamlit as st
import math

with st.form("my_form"):
   st.write("SecOps Details")
   ingestDaily = st.number_input('Daily Ingest in gigabytes', value=0)
   license = st.selectbox('Select your license package', ['SecOps Enterprise','SecOps Enterprise+'])
   st.form_submit_button('Submit my picks')

ingestAnnual = ingestDaily * 365
ingestAnnualTB = ingestAnnual * .001

if ingestAnnualTB > 100:
	if license == "SecOps Enterprise": 
		cost = ingestAnnualTB * 2400
	if license == "SecOps Enterprise+":
		cost = ingestAnnualTB * 4600
else cost = 0
ingestFormatted = math.ceil(ingestAnnualTB)

# This is outside the form
with st.container(border=True):
	st.write()
	st.write("Selected License: ", license)
	st.write("Annual Ingest in Tb: {:0,.0f}".format(ingestFormatted))
	st.write("Calculated Annual Contract Value, List: ${:0,.0f}".format(cost).replace('$-','-$'))
