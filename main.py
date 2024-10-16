import streamlit as st
import math

with st.form("my_form"):
	st.subheader("SecOps Details",divider=True)
	metric = st.radio('What ingestion metric will be used?',['Gb/day','Tb/year'], index=None)
	ingest = st.number_input('Ingest Number, based on metric selected above', value=0)
	license = st.radio('Select your license package', ['SecOps Enterprise','SecOps Enterprise+'])
	discount = st.number_input('Percentage discount, in whole numbers.', value=0)
	customerSuccess = st.radio("Which SecOps Customer Success package will be quoted?",["Expert","Expert+","None"])
	st.form_submit_button('Submit my picks')

# secops = []
# [metric, ingest, license, discount, customerSuccess]
if metric == 'Gb/day': 
	ingestAnnual = ingest * 365
	ingestAnnualTB = ingestAnnual * .001
else:
	ingestAnnualTB = ingest

if license == "SecOps Enterprise": 
	listPrice = ingestAnnualTB * 2400
elif license == "SecOps Enterprise+":
	listPrice = ingestAnnualTB * 4600

if discount > 0: 
	quotePrice = listPrice * (discount / 100 )
else: 
	quotePrice = listPrice


ingestFormatted = math.ceil(ingestAnnualTB)
#csRec = "Please consider attaching Customer Success Expert or Expert+ to this deal."

# This is outside the form
with st.container(border=True):
	st.subheader("Budgetary Deal Numbers", divider=True)
	if license == "SecOps Enterprise+" and quotePrice < 400000: 
		st.write("For SecOps Enterprise+ deals, the minimum post-discount price must be $400k or higher.")
		st.write("Est SecOps ACV: ${:0,.0f}".format(quotePrice).replace('$-','-$'))
	elif ingestAnnualTB > 100 and quotePrice > 100000: 
		#st.write()
		st.write("Selected License: ", license)
		st.write("Annual Ingest in Tb: {:0,.0f}".format(ingestFormatted))
		st.write("Discount Applied: ", discount)
		st.write("Est SecOps ACV: ${:0,.0f}".format(quotePrice).replace('$-','-$'))
		if customerSuccess == "None": 
			st.write("Please consider attaching Customer Success Expert or Expert+ to this deal.")
		else: 
			st.write("Customer Success Package: ", customerSuccess)
		
			
	else: 
		st.write("This deal does not meet minimum deal size requirements.")
