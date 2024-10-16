
def socalc(metric,ingest, license, discount, customerSuccess): 
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

  return quotePrice




# secops = []
# [metric, ingest, license, discount, customerSuccess]
