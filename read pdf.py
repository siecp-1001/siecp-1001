
import PyPDF2 
from PyPDF2 import PdfFileReader
pdf= open("Building Chatbots with Python_ Using Natural Language Processing and Machine Learning ( PDFDrive ).pdf","rb")
pdf_reader =PyPDF2.PdfFileReader(pdf)
print(pdf_reader.numPages)
page=pdf_reader.getPage(0)
print(page.extractText())

pdf.close()