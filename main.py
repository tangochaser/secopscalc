import streamlit as st
import math

st.header("SecOps Deal Calculator")
with st.form("my_form"):
	st.subheader("SecOps Product",divider=True)
	metric = st.radio('What ingestion metric will be used?',['Gb/day','Tb/year'], index=None)
	ingest = st.number_input('Ingest Number, based on metric selected above', value=0)
	license = st.radio('Select your SecOps license tier', ['Enterprise','Enterprise+'], index=None)
	discount = (st.number_input('Percentage discount, in whole numbers.', value=0, key="sod") / 100)
	st.divider()
	st.subheader("Customer Success",divider=True)
	csPackage = st.radio("Which SecOps Customer Success package will be quoted?",["Expert","Expert+","None"], index=None)
	csDiscount = (st.number_input('Percentage discount, in whole numbers.', value=0, key="csd") / 100)
	st.form_submit_button('Submit my picks')

# secops = []
# [metric, ingest, license, discount, csPackage]

listPrice = 0
ingestAnnualTB = 0
entList = 2400
entPlusList = 4600
csExpertList = 100000
csExpertPlusList = 250000
incorrectEntry = False
badDiscount = False

if metric == 'Gb/day': 
	ingestAnnual = ingest * 365
	ingestAnnualTB = ingestAnnual * .001
elif metric == 'Tb/day':
	ingestAnnualTB = ingest


if metric is not None and ingest > 0: 
	incorrectEntry = True


if license == "Enterprise": 
	listPrice = ingestAnnualTB * entList
elif license == "Enterprise+":
	listPrice = ingestAnnualTB * entPlusList

if (metric is not None and license is None) or (metric is None and license is not None):
	incorrectEntry = True

if 80 > discount > 22: 
	quotePrice = listPrice * discount
elif discount == 0: 
	quotePrice = listPrice
else: 
	badDiscount = True


if csPackage == "Expert": 
	csList = csExpertList
elif csPackage == "Expert+":
	csList = csExpertPlusList
	
ingestFormatted = math.ceil(ingestAnnualTB)
#csRec = "Please consider attaching Customer Success Expert or Expert+ to this deal."

# This is outside the form
with st.container(border=True):
	st.subheader("Budgetary Deal Numbers", divider=True)

	if metric is None and ingest == 0 and license is None and discount == 0: 
		st.write("Please fill out the form above.") 
	
	elif incorrectEntry == True: 
		st.write("The form was not filled out correctly. Please ensure both the ingestion metric and the license tier are selected and entered in.")

	elif badDiscount == True: 
		st.write("You entered an invalid discount level. Please enter a number above 22% and below 80%.")
	
	elif license == "SecOps Enterprise+" and quotePrice < 400000: 
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
		
