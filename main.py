import streamlit as st
import math

with st.form("my_form"):
	st.subheader("SecOps Details",divider=True)
	metric = st.radio('What ingestion metric will be used?',['Gb/day','Tb/year'], index=None)
	ingest = st.number_input('Ingest Number, based on metric selected above', value=0)
	license = st.radio('Select your license package', ['SecOps Enterprise','SecOps Enterprise+'])
	discount = (st.number_input('Percentage discount, in whole numbers.', value=0) / 100)
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
	quotePrice = listPrice * discount
else: 
	quotePrice = listPrice

licShort_e = "Ent"
licShort_eplus = "Ent+"

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
		#st.write("Selected License: ", license)
		#st.write("Annual Ingest in Tb: {:0,.0f}".format(ingestFormatted))
		#st.write("Discount Applied: {:.0%}".format(discount))
		#st.write("Est SecOps ACV: ${:0,.0f}".format(quotePrice).replace('$-','-$'))
		#st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")
		col1, col2, col3 = st.columns(3)
		col1 = st.metric("SecOps License", license, delta=None)
		col2 = st.metric("Annual Ingest, Tb", ingestFormatted, delta=None)
		col3 = st.metric("Discount", "{:0,.0%}".format(discount*100))
		st.metric("Estimated SecOps ACV", "${:0,.0f}".format(quotePrice), delta=None)
		if customerSuccess == "None": 
			st.write("Please consider attaching Customer Success Expert or Expert+ to this deal.")
		else: 
			st.write("Customer Success Package: ", customerSuccess)
		
			
	else: 
		st.write(":red[**This deal does not meet minimum deal size requirements.**]")
		st.write("Annual Ingest in Tb: {:0,.0f}".format(ingestFormatted))
		if ingestFormatted < 100: 
			st.markdown(":red[*Annual Ingest is below 100Tb.*]")
		st.write("Est SecOps ACV: ${:0,.0f}".format(quotePrice).replace('$-','-$'))
		if quotePrice < 100000: 
			st.markdown(":red[*Quoted ACV is below $100,000.*]")
		
