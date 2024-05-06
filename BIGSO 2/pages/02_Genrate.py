from docxtpl import DocxTemplate
import pandas as pd 
import streamlit as st
from datetime import date 


today=date.today()
print(today)
details=pd.read_csv('machine_details.csv').values.tolist()
details2=pd.read_csv('company_details.csv').values.tolist()
doc=DocxTemplate("Machine_Quot.docx")
lists=[]
gst=0
total=0
qot_no=st.text_input("Quot no:")


def read_word_document(qot_no):
    with open(f"quot/{qot_no}.docx", "rb") as file:
        docx_content = file.read()
    return docx_content

# Render download button

if qot_no:
    for i in details:
        
        if int(i[0])==int(qot_no):
            print()
            prize=i[6]
            gst=i[7]
            total=i[8]
            width=i[2]
            circumference=i[3]
            features=i[4]
            i=i[1:7]
            lists.append(i)
    for i in details2:
        print(int(i[5]))
        if int(i[5])==int(qot_no):
            gstin=i[4]
    print(lists)
    

    
    doc.render({"quot":str(qot_no).zfill(3),"prize":prize,"width":width,"circumference":circumference,"features":features,"gst":gst,"total":total,"gstin":gstin,"date":str(today)})
    doc.save(f"quot/{qot_no}.docx")
    docx_content = read_word_document(qot_no)
    st.download_button(label="Download Quotation", data=docx_content, file_name=f"quot/{qot_no}.docx", mime="application/docx")