import streamlit as st
import math

with st.form("my_form"):
	st.write("SecOps Details")
	ingestDaily = st.number_input('Daily Ingest in gigabytes', value=0)
	license = st.selectbox('Select your license package', ['SecOps Enterprise','SecOps Enterprise+'])
	discount = st.number_input('Percentage discount, in whole numbers.')
	st.form_submit_button('Submit my picks')
   

ingestAnnual = ingestDaily * 365
ingestAnnualTB = ingestAnnual * .001


if license == "SecOps Enterprise": 
	listPrice = ingestAnnualTB * 2400
if license == "SecOps Enterprise+":
	listPrice = ingestAnnualTB * 4600

quotePrice = (listPrice * (discount * .01, 2))

ingestFormatted = math.ceil(ingestAnnualTB)
customerSuccess = "Please consider attaching Customer Success Expert or Expert+ to this deal."

# This is outside the form
with st.container(border=True):
	if license == "SecOps Enterprise+" and cost < 400000: 
		st.write("For SecOps Enterprise+ deals, the minimum post-discount price must be $400k or higher.")
		#st.write("You can change the 
	elif ingestAnnualTB > 100: 
		#st.write()
		st.write("Selected License: ", license)
		st.write("Annual Ingest in Tb: {:0,.0f}".format(ingestFormatted))
		st.write("Calculated Annual Contract Value, List: ${:0,.0f}".format(cost).replace('$-','-$'))
		st.write(customerSuccess)
	else: 
		st.write("This deal does not meet minimum deal size requirements.")
