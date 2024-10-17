import streamlit as st
import math

st.header("SecOps Deal Calculator")
with st.form("my_form"):
	st.subheader("SecOps Product",divider=True)
	metric = st.radio('What ingestion metric will be used?',['Gb/day','Tb/year'], index=None)
	ingest = st.number_input('Ingest Number, based on metric selected above', value=0)
	license = st.radio('Select your SecOps license tier', ['Enterprise','Enterprise+'])
	discount = (st.number_input('Percentage discount, in whole numbers.', value=0) / 100)
	st.divider()
	st.subheader("Customer Success",divider=True)
	csPackage = st.radio("Which SecOps Customer Success package will be quoted?",["Expert","Expert+","None"])
	csDiscount = (st.number_input('Percentage discount, in whole numbers.', value=0) / 100)
	st.form_submit_button('Submit my picks')

# secops = []
# [metric, ingest, license, discount, csPackage]

if metric == 'Gb/day': 
	ingestAnnual = ingest * 365
	ingestAnnualTB = ingestAnnual * .001
else:
	ingestAnnualTB = ingest

if license == "Enterprise": 
	listPrice = ingestAnnualTB * 2400
elif license == "Enterprise+":
	listPrice = ingestAnnualTB * 4600

if discount > 0: 
	quotePrice = listPrice * discount
else: 
	quotePrice = listPrice

if csPackage == "Expert": 
	csList = 100000
elif csPackage == "Expert+":
	csList = 250000
	
ingestFormatted = math.ceil(ingestAnnualTB)
#csRec = "Please consider attaching Customer Success Expert or Expert+ to this deal."

# This is outside the form
with st.container(border=True):
	st.subheader("Budgetary Deal Numbers", divider=True)
	if license == "SecOps Enterprise+" and quotePrice < 400000: 
		st.write("For SecOps Enterprise+ deals, the minimum post-discount price must be $400k or higher.")
		st.write("Est SecOps ACV: ${:0,.0f}".format(quotePrice).replace('$-','-$'))

	elif ingestAnnualTB > 100 and quotePrice > 100000: 
		st.metric("**Estimated SecOps ACV**", "${:0,.0f}".format(quotePrice), delta=None)
		col1, col2, col3 = st.columns(3)
		col2.metric("**SecOps License**", license, delta=None)
		col1.metric("**Annual Ingest, Tb**", ingestFormatted, delta=None)
		col3.metric("**SecOps Discount**", "{:0,.0%}".format(discount))
		st.divider()
		st.write("****Customer Success Package****")
		if csPackage != "None":
			cscol1, cscol2, cscol3 = st.columns(3)
			cscol2.metric("**Customer Success Tier**", csPackage)
			cscol1.metric("**CS ACV**", csList * csDiscount)
			cscol3.metric("**CS Discount**", "{:0,.0%}".format(csDiscount))
		elif csPackage == "None": 
			st.write("Please consider attaching Customer Success Expert or Expert+ to this deal.")
			
	else: 
		st.write(":red[**This deal does not meet minimum deal size requirements.**]")
		st.write("Annual Ingest in Tb: {:0,.0f}".format(ingestFormatted))
		if ingestFormatted < 100: 
			st.markdown(":red[*Annual Ingest is below 100Tb.*]")
		st.write("Est SecOps ACV: ${:0,.0f}".format(quotePrice).replace('$-','-$'))
		if quotePrice < 100000: 
			st.markdown(":red[*Quoted ACV is below $100,000.*]")
		
