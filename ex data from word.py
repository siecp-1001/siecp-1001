import docx
from docx import Document
doc=open("assignment-section.docx","rb")
document=docx.Document(doc)
docu=""
for para in document.paragraphs:
    docu += para.text 
print(docu)    