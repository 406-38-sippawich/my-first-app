import streamlit as st

st.markdown("# :green[Doung Café ]")
st.write("ยินดีต้อนรับเข้าสู่ :green[Doung Café] กรุณาเลือกสินค้าของคุณ")
st.write("Welcome to :green[Doung Café] Please select your order")
Espresso_count = st.number_input('Espresso เอสเพรสโซ (แก้ว)' ,value = 0)
Americano_count = st.number_input('Americano อเมริกาโน (แก้ว)' ,value = 0)
Latte_count = st.number_input('Latte ลาเต้ (แก้ว)' ,value = 0)
Cappuccino_count = st.number_input('Cappuccino คาปูชิโน (แก้ว)' ,value = 0)
Mocha_count = st.number_input('Mocha มอคค่า (แก้ว)' ,value = 0)
IcedCoffee_count = st.number_input('Iced Coffee กาแฟเย็น (แก้ว)' ,value = 0)
Croissant_count = st.number_input('🥐Croissant ครัวซองต์ (ชิ้น)' ,value = 0)
Cheesecake_count = st.number_input('🍰Cheesecake ชีสเค้ก (ชิ้น)' ,value = 0)
count_sum = IcedCoffee_count + Mocha_count + Cappuccino_count + Latte_count + Americano_count + Espresso_count + Croissant_count + Cheesecake_count
if Espresso_count < 0 :
  st.error(':red[Error จำนวนสินค้าไม่สามารถติดลบได้]')
elif Americano_count < 0 :
  st.error(':red[Error จำนวนสินค้าไม่สามารถติดลบได้]')
elif Latte_count < 0:
  st.error(':red[Error จำนวนสินค้าไม่สามารถติดลบได้]')
elif Cappuccino_count < 0:
  st.error(':red[Error จำนวนสินค้าไม่สามารถติดลบได้]')
elif Mocha_count < 0:
  st.error(':red[Error จำนวนสินค้าไม่สามารถติดลบได้]')
elif IcedCoffee_count < 0:
  st.error(':red[Error จำนวนสินค้าไม่สามารถติดลบได้]')
elif Croissant_count < 0:
  st.error(':red[Error จำนวนสินค้าไม่สามารถติดลบได้]')
elif Cheesecake_count < 0:
  st.error(':red[Error จำนวนสินค้าไม่สามารถติดลบได้]')
else:
  st.write(f'☕🥐🍰จำนวนสินค้า :green[{count_sum}] ชิ้น')
Espresso_cost = 45 * Espresso_count
Americano_cost = 45 * Americano_count
Latte_cost = 50 * Latte_count
Cappuccino_cost = 50 * Cappuccino_count
Mocha_cost = 55 * Mocha_count
IcedCoffee_cost = 60 * IcedCoffee_count
Croissant_cost = 45 * Croissant_count
Cheesecake_cost = 60 * Cheesecake_count
cost = IcedCoffee_cost + Mocha_cost + Cappuccino_cost + Latte_cost + Americano_cost + Espresso_cost + Croissant_cost + Cheesecake_cost
if Espresso_count < 0 :
  st.error(':red[Error ราคาสินค้าไม่สามารถติดลบได้]')
elif Americano_count < 0 :
  st.error(':red[Error ราคาสินค้าไม่สามารถติดลบได้]')
elif Latte_count < 0:
  st.error(':red[Error ราคาสินค้าไม่สามารถติดลบได้]')
elif Cappuccino_count < 0:
  st.error(':red[Error ราคาสินค้าไม่สามารถติดลบได้]')
elif Mocha_count < 0:
  st.error(':red[Error ราคาสินค้าไม่สามารถติดลบได้]')
elif IcedCoffee_count < 0:
  st.error(':red[Error ราคาสินค้าไม่สามารถติดลบได้]')
elif Croissant_count < 0:
  st.error(':red[Error ราคาสินค้าไม่สามารถติดลบได้]')
elif Cheesecake_count < 0:
  st.error(':red[Error ราคาสินค้าไม่สามารถติดลบได้]')
else:
  st.write(f'💵:green[ราคาสินค้า {cost} บาท] :yellow[(ยังไม่คิด VAT และ ลดราคา)]')
st.write('🏷️:green[ซื้อครบ 300 บาท ลด 10%!!!]')
st.divider()
discount_sum = 1
if cost > 300:
  discount_sum -= 0.10
membership = st.text_input("🪪Do you have a membership? คุณได้สมัครสามาชิกไหม? (Normal/Gold/Platinum(ไม่มีให้เว้นว่าง))" , value= " " , )
l_membership = membership.strip().lower()
if l_membership == 'normal' :
  discount_sum -= 0.05
elif l_membership == 'gold' :
  discount_sum -= 0.10
elif l_membership == 'platinum' :
  discount_sum -= 0.15
student = st.text_input("📚Are you a student? คุณเป็นนักศึกษาใช่ไหม?(Yes/No)" , value= "No" , )
l_student = student.strip().lower()
if l_student == 'yes' :
  discount_sum -= 0.10
st.divider()
dis_cost = cost * discount_sum
VAT_cost = dis_cost * 1.07
st.write(f'💵:green[ราคาสินค้า {VAT_cost} บาท] :yellow[(คิด VAT และ ลดราคาแล้ว)]')
money = st.number_input('💳กรุณาจ่ายเงิน' ,value = 0.00)
change = money - VAT_cost
if change < 0 :
  st.write('❌💵:red[คุณมีเงินไม่เพียงพอ]')
else:
  st.write(f'💸:green[เงินทอน {change} บาท]')
