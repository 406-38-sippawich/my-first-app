import streamlit as st
#1
st.markdown("# :red[💪 แอปพลิเคชั่นคำนวณค่าดัชนีมวลกาย (BMI) 🏋️]")
st.write("⚖️📏 กรุณากรอกข้อมูลน้ำหนักและส่วนสูง 🩺 เพื่อเช็คสุขภาพเบื้องต้น ❤️")

#2
weight = st.number_input('⚖️ กรุณากรอกน้ำหนัก (Kg)')
height_cm = st.number_input('📏 กรุณากรอกส่วนสูง (Cm)')

#3
if st.button('📊 คำนวณค่า BMI'):
  height_m = height_cm / 100
  BMI = weight / (height_m ** 2)
  
  st.write("---")
  st.header(f'ค่า BMI ของคุณคือ: **{bmi:.2f}**')

#4
if BMI < 18.5:
  st.warning('🚨 คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม) ⚠️')
elif 18.5 <= BMI < 23.0:
  st.success('✅ คุณมีน้ำหนักในเกณฑ์ปกติ (สุขภาพดี) 🎉')
elif 23.0 <= BMI < 25.0:
  st.info('🍎 คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม) 🥗')
else:
  st.error('🏃💧 คุณมีน้ำหนักในเกณฑ์อ้วน ควรออกกำลังกายและระวังเรื่องการกิน')

#5
st.divider()
st.write('นายสิปปวิชญ์ พิบูลย์ ม.4/6 เลขที่ 38')
