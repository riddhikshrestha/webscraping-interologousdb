# @Author: Riddhi Shrestha
# web: www.riddhishrestha.com.np
import requests
from bs4 import BeautifulSoup
import csv

# Our Actual Url to scrap

response = requests.get('http://ophid.utoronto.ca/ophidv2.204/ForwardingServlet?inputFormat=SWISSPROT_ID&ophidOrganism=HUMAN&outputFormat=htmlOutput&proteins=P50851#protein%20P50851')

soup = BeautifulSoup(response.text,'html.parser')

# To Export Data into CSV

outfile = open('i2d.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(["UniProtKB ID", "HGNC","PPI I2D"])

uniprotid=soup.find('a',target='SwissProt').get_text()
hngc=soup.find('a',target='GeneCards').get_text()
# print(uniportid)

for i2d in soup.find_all('span', attrs={'class': 'redLink'}):
	ppi2d=i2d.get_text()
	writer.writerow([uniprotid, hngc,ppi2d])
    # print(uniportid,?hngc,ppi2d)
outfile.close()


