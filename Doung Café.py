import streamlit as st

st.markdown("# :green[💪 Doung Café 🏋️]")
st.write("ยินดีต้อนรับเข้าสู่ :green[Doung Café] กรุณาเลือกสินค้าของคุณ")
st.write("Welcome to :green[Doung Café] Please select your order")
Espresso_count = st.number_input('Espresso เอสเพรสโซ (แก้ว)' ,value = 0)
Americano_count = st.number_input('Americano อเมริกาโน (แก้ว)' ,value = 0)
Latte_count = st.number_input('Latte ลาเต้ (แก้ว)' ,value = 0)
Cappuccino_count = st.number_input('Cappuccino คาปูชิโน (แก้ว)' ,value = 0)
Mocha_count = st.number_input('Mocha มอคค่า (แก้ว)' ,value = 0)
IcedCoffee_count = st.number_input('Iced Coffee กาแฟเย็น (แก้ว)' ,value = 0)
Croissant_count = st.number_input('Croissant ครัวซองต์ (ชิ้น)' ,value = 0)
Cheesecake_count = st.number_input('Cheesecake ชีสเค้ก (ชิ้น)' ,value = 0)
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
  st.write(f'จำนวนสินค้า {count_sum} ชิ้น')
membership = st.text.input("Do you have a membership? คุณได้สมัครสามาชิกไหม? (Normal/Gold/Platinum(ไม่มีให้เว้นว่าง))
st.write(f'{membership}')

