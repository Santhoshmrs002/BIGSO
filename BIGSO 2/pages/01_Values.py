import streamlit as st
import pandas as pd
import json 


with open("quot_no.json","r") as f:
    quot_no=str(json.load(f)["q"]).zfill(3)
st.subheader("Quotation number: "+quot_no)
company_name=st.text_input('COMPANY NAME:')
location=st.text_input('LOCATION:')
mobile_number=st.text_input('MOBILE NUMBER:')
email=st.text_input('EMAIL:')
gstin=st.text_input('GSTIN:')

if st.button("Submit"):
    data= {'company_name': [company_name], 'location': [location], 'mobile_number': [mobile_number],'email':[email],'gstin':[gstin],'qut_no':[quot_no]}

    df=pd.DataFrame(data)
    file_path="company_details.csv"
    df.to_csv(file_path, mode='a', header=False, index=False)
#quot_no=st.text_input("Quotation number:")

st.header("Color:")
no_color=st.selectbox('Number of colour:', ['1','2','3','4','6','8'])


st.header('Width')
c1,c2=st.columns(2)
with c1:
    width_value = st.number_input('Width', min_value=0, step=1)
with c2:
    width_unit = st.selectbox('Width Unit', ['inch', 'mm'])
width=str(width_value)+" "+width_unit

st.header('Circumference')
cc1,cc2=st.columns(2)
with cc1:
    circumference_value = st.number_input('Circumference', min_value=0.0, step=0.1)
with cc2:
    circumference_unit = st.selectbox('Circumference Unit', ['inch', 'mm'])
circumference=str(circumference_value)+" "+circumference_unit

st.header("Equipments")
options=["Gearbox motor","Delta Drive","Hot Air Blowing System","Digital Piece Counting","Control Drum winder","Electronic Anilox Roller","Rubber Rollers","steel  Rollers","Air shaft","Web Aligner & Edge Guiding System","Automatic tension controller","Automatic Lifting Hoist","Cylinder"]
equipments_options = st.multiselect('Equipments:', options)
sc1,sc2=st.columns(2)
with sc1:
    sizes=['9','10','11','12','14','16','18','20']
    size_of_cylinder=st.multiselect("cylinder sizes:",sizes)
with sc2:
    unit_of_cylinder=st.selectbox('cylinder Unit', ['inch', 'mm'])
cylinder_size=",".join(['"{}"'.format(item+unit_of_cylinder) for item in size_of_cylinder])

st.header("Prize")
prize=st.text_input("Prize Amount:")

if st.button("Save"):
    data= {'qut_no': [quot_no], 'no_of_color': [no_color], 'width': [width],'circumference':[circumference],'equipments':[equipments_options],'cylinder_size':[cylinder_size],'prize':[prize],"gst":[int(prize)*(18/100)],"total":[int(prize)+int(prize)*(18/100)]}

    df=pd.DataFrame(data)
    file_path="machine_details.csv"
    df.to_csv(file_path, mode='a', header=False, index=False)
    with open("quot_no.json","w") as f:
        json.dump({"q":int(quot_no)+1},f)
df1=pd.read_csv('machine_details.csv')
df1.index=df1.index+1
st.write(df1)