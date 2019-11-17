import os, PyPDF2
from os import path
userfilename="FinalReport"
pdf2merge=[]
# for filename in os.listdir('.'):
# 	if filename.endswith('.pdf'):
# 		print filename
# 		pdf2merge.append(filename)
pdf2merge.append('first_page.pdf')
if(path.exists("nmap_scan.txt.pdf")==True): 
	pdf2merge.append('nmap_scan.txt.pdf')
if(path.exists("drupe_scan.txt.pdf")==True): 
	pdf2merge.append('drupe_scan.txt.pdf')
if(path.exists("wp_scan.txt.pdf")==True): 
	pdf2merge.append('wp_scan.txt.pdf')
if(path.exists("joom_scan.txt.pdf")==True): 
	pdf2merge.append('joom_scan.txt.pdf')
pdfWriter = PyPDF2.PdfFileWriter()
# print pdf2merge
for filename in pdf2merge:
	pdfFileObj=open(filename,'rb')
	pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)
pdfOutput = open(userfilename+'.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
