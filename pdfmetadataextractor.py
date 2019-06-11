#!/usr/bin/python

import pyPdf
import argparse
from pyPdf import PdfFileReader
def metareader(pdfFile):
	pdffile = PdfFileReader(file(pdfFile,'rb'))
	metadata = pdffile.getDocumentInfo()
	for data in metadata:
		print("[+]" + data + " : " + metadata[data])
		
def main():
	parser  = argparse.ArgumentParser()
	parser.add_argument("-f","--pdf",required=True,type=str,help="Enter pdf file")
	args = parser.parse_args()
	argfile = args.pdf
	metareader(argfile)
if __name__ == "__main__":
	main()

	
