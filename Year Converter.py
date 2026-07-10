import streamlit as st
st.title('App แปลง ปี พ.ศ. เป็น ปี ค.ศ.')
BH_year = st.number_input('กรุณากรอกปี พ.ศ. ที่ต้องการแปลง' ,value = 2569)
CE_year = BH_year - 543
st.header(f'ปี ค.ศ. = {CE_year}')
