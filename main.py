import streamlit as st
import math

with st.form("my_form"):
	st.write("SecOps Details")
	metric = st.radio('What ingestion metric will be used?',['Gb/day','Tb/year'])
	if metric == 'Gb/day': 
		ingestDaily = st.number_input('Daily Ingest in gigabytes', value=0)
	if metric == 'Tb/year':
		ingestAnnual = st.number_input('Annual Ingest in terbytes', value=0)
	license = st.selectbox('Select your license package', ['SecOps Enterprise','SecOps Enterprise+'])
	discount = st.number_input('Percentage discount, in whole numbers.', value=0)
	customerSuccess = st.radio("Which SecOps Customer Success package will be quoted?",["Expert","Expert+","None"])
	st.form_submit_button('Submit my picks')
   

ingestAnnual = ingestDaily * 365
ingestAnnualTB = ingestAnnual * .001


if license == "SecOps Enterprise": 
	listPrice = ingestAnnualTB * 2400
if license == "SecOps Enterprise+":
	listPrice = ingestAnnualTB * 4600

if discount > 0: 
	quotePrice = listPrice * (discount / 100 )
else: 
	quotePrice = listPrice

ingestFormatted = math.ceil(ingestAnnualTB)
customerSuccess = "Please consider attaching Customer Success Expert or Expert+ to this deal."

# This is outside the form
with st.container(border=True):
	st.write("Budgetary Deal Numbers")
	if license == "SecOps Enterprise+" and quotePrice < 400000: 
		st.write("For SecOps Enterprise+ deals, the minimum post-discount price must be $400k or higher.")
		#st.write("You can change the 
	elif ingestAnnualTB > 100: 
		#st.write()
		st.write("Selected License: ", license)
		st.write("Annual Ingest in Tb: {:0,.0f}".format(ingestFormatted))
		st.write("Calculated Annual Contract Value, List: ${:0,.0f}".format(quotePrice).replace('$-','-$'))
		st.write(customerSuccess)
	else: 
		st.write("This deal does not meet minimum deal size requirements.")
